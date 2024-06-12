import os
import json
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


def get_image(templates):
    images_urls = templates.get('imgs', [])
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


def load_place_from_json(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка при загрузке данных из файла {json_file}: {e}")
        return None


def load_places_from_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_file = os.path.join(directory, filename)
            template = load_place_from_json(json_file)
            if template:
                load_place_to_admin_panel(template)


def load_place_to_admin_panel(template):
    images = get_image(template)
    place, created = Place.objects.get_or_create(
        title=template.get('title'),
        description_short=template.get('description_short'),
        description_long=template.get('description_long'),
        lng=template.get('coordinates', {}).get('lng'),
        lat=template.get('coordinates', {}).get('lat'),
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
    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Путь к папке с JSON файлами')

    def handle(self, *args, **kwargs):
        directory = kwargs['directory']
        if not os.path.exists(directory):
            self.stdout.write(self.style.ERROR(f'Папка {directory} не существует.'))
            return

        load_places_from_directory(directory)
