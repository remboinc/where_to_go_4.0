from django.shortcuts import render
from .models import Place


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
                "description_short": place.description_short,
                "description_long": place.description_long,
                "placeId": place.id,
                "detailsUrl": {
                    'title': place.title,
                    'description_short': place.description_short,
                    'description_long': place.description_long,
                    'imgs': []
                }
            }
        }
        features.append(feature)

    return render(request, 'index.html', {'places_geojson': features})
