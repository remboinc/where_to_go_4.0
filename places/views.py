from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
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
                "detailsUrl": f"/places/{place.id}/"
            }
        }
        features.append(feature)

    return render(request, 'index.html', {'places_geojson': features})


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    imgs = [img.get_absolute_image_url for img in place.media.all()]
    data = {
        'title': place.title,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'imgs': imgs
    }

    return JsonResponse(data, content_type='application/json', json_dumps_params={'ensure_ascii': False, 'indent': 2})
