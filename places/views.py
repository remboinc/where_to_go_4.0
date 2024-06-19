from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place, PlaceImage


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "description_short": place.short_description,
                "description_long": place.long_description,
                "placeId": place.id,
                "detailsUrl": reverse('place_detail', kwargs={'place_id': place.id})
            }
        }
        features.append(feature)

    return render(request, 'index.html', {'places_geojson': features})


def place_detail(request, place_id):
    place = get_object_or_404(Place.objects.select_related(), pk=place_id)
    imgs = [img.get_absolute_image_url for img in place.media.all()]
    serialize_place = {
        'title': place.title,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'imgs': imgs
    }

    return JsonResponse(serialize_place, content_type='application/json', json_dumps_params={'ensure_ascii': False, 'indent': 2})
