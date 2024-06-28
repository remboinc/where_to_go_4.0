import json
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage
from django.core.exceptions import MultipleObjectsReturned


def get_images(images_urls):
    images = []
    for image_url in images_urls:
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            b_image = response.content
            images.append(b_image)
            print(f'Изображение успешно загружено: {image_url}')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при загрузке изображения {image_url}: {e}')
    return images


def load_place_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f'Данные успешно загружены из URL: {url}')
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при загрузке данных из URL {url}: {e}')
    except json.JSONDecodeError as e:
        print(f'Ошибка при парсинге JSON из URL {url}: {e}')


def load_place_to_admin_panel(template):
    images = get_images(template.get('imgs', []))
    try:
        place, created = Place.objects.get_or_create(
            title=template.get('title'),
            defaults={
                'short_description': template.get('description_short'),
                'long_description': template.get('description_long'),
                'lng': template.get('coordinates', {}).get('lng'),
                'lat': template.get('coordinates', {}).get('lat'),
            }
        )
    except MultipleObjectsReturned:
        places = Place.objects.filter(title=template.get('title'))
        place = places.first()
        created = False
        print(f'Найдено несколько мест с заголовком "{template.get("title")}". Используется первый найденный.')

    if created:
        print('Новый объект был создан.')
        for index, b_image in enumerate(images):
            image_name = f'{place.id}_{index}.jpg'
            image_of_place = PlaceImage.objects.create(place=place)
            try:
                image_of_place.image.save(image_name, ContentFile(b_image), save=True)
                print(f'Изображение {image_name} успешно сохранено.')
            except Exception as e:
                print(f'Ошибка при сохранении изображения {image_name}: {e.__class__.__name__} - {e}')
    else:
        print('Объект был найден в базе данных.')

    print(f'Объект имеет ID: {place.id}')


class Command(BaseCommand):
    help = 'Load place data from a JSON file URL'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL JSON-файла с данными места')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        template = load_place_from_url(url)
        if template:
            load_place_to_admin_panel(template)
