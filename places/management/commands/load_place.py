import json
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


def get_image(images_urls):
    images = []
    for image_url in images_urls:
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            b_image = response.content
            images.append(b_image)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при загрузке изображения {image_url}: {e}")
    return images


def load_place_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке данных из URL {url}: {e}")
        return None


def load_place_to_admin_panel(template):
    images = get_image(template.get('imgs', []))
    place, created = Place.objects.get_or_create(
        title=template.get('title'),
        defaults={
            'short_description': template.get('description_short'),
            'long_description': template.get('description_long'),
            'lng': template.get('coordinates', {}).get('lng'),
            'lat': template.get('coordinates', {}).get('lat'),
        }
    )

    if created:
        print('Новый объект был создан.')
        for index, b_image in enumerate(images):
            image_name = f'{place.title}_{place.id}_{index}.jpg'
            image_of_place = PlaceImage.objects.create(
                place=place,
                title=image_name,
            )
            try:
                image_of_place.image.save(image_name, ContentFile(b_image), save=True)
            except Exception as e:
                print(f"Ошибка при сохранении изображения {image_name}: {e}")
    else:
        print('Объект был найден в базе данных.')

    print('Объект имеет ID:', place.id)


class Command(BaseCommand):
    help = 'Load place data from a JSON file URL'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='The URL of the JSON file containing place data')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        template = load_place_from_url(url)
        if template:
            load_place_to_admin_panel(template)
