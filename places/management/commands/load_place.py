import json
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage
from django.core.exceptions import MultipleObjectsReturned


def load_place_to_admin_panel(template):
    try:
        place, created = Place.objects.get_or_create(
            title=template['title'],
            defaults={
                'short_description': template['description_short'],
                'long_description': template['description_long'],
                'lng': template['coordinates']['lng'],
                'lat': template['coordinates']['lat'],
            }
        )
    except MultipleObjectsReturned:
        places = Place.objects.filter(title=template['title'])
        place = places.first()
        created = False
        print(f'Найдено несколько мест с заголовком "{template["title"]}". Используется первый найденный.')

    if created:
        print('Новый объект был создан.')
        for index, image_url in enumerate(template['imgs']):
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                b_image = response.content
                image_name = f'{place.id}_{index}.jpg'
                image_of_place = PlaceImage.objects.create(place=place)
                image_of_place.image.save(image_name, ContentFile(b_image), save=True)
                print(f'Изображение {image_name} успешно сохранено.')
            except requests.exceptions.RequestException as e:
                print(f'Ошибка при загрузке изображения {image_url}: {e}')
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

        try:
            response = requests.get(url)
            response.raise_for_status()
            print(f'Данные успешно загружены из URL: {url}')
            template = response.json()
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при загрузке данных из URL {url}: {e}')
            return
        except json.JSONDecodeError as e:
            print(f'Ошибка при парсинге JSON из URL {url}: {e}')
            return

        if template:
            load_place_to_admin_panel(template)