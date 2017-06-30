from django.shortcuts import render, HttpResponse

from visualisation.models import Country, Date, MigrationEvent
# from haystack.query import SearchQuerySet
# from haystack.inputs import AutoQuery
from django.http import JsonResponse


def countryUpdate(request):
    name = request.GET.get('name')
    country = Country.objects.get(border__name=name)
    years = []
    buttons = ''
    for e in MigrationEvent.objects.filter(origin=country):
        if e.recognisedrate > 0:
            if e.date.year not in years:
                years.append(e.date.year)
    years = sorted(years)
    for y in years:
        buttons += '<input type="button" value="' + str(y) + '"  \
        onclick="updateMigrationLater(' + str(country.id) + ',' + str(y) + ')" \
        ></input>'

    return HttpResponse('<h1>' + country.name + '</h1>' + buttons)


# Department view
def mapview(request):
    context = {
        'test': 'test',
    }
    return render(request, 'visualisation/map.html', context)

# Commented out to stop flake8 moanint - no views yet!
# from django.shortcuts import render


def mapCountry(request, id):
    context = {}
    country = Country.objects.get(pk=id)
    context['country'] = country
    return render(request, 'visualisation/map.html', context)


def migrationLayer(request, id, year):
    migLayers = []
    lyr = {}
    lyr['data'] = []
    origin = Country.objects.get(pk=id)
    origPoint = [origin.border.the_geom.centroid.x,
                 origin.border.the_geom.centroid.y]
    yr = Date.objects.get(year=year)
    events = MigrationEvent.objects \
        .filter(date=yr).filter(origin=origin)
    for e in events:
        if e.recognisedrate > 0:
            destPoint = [e.destination.border.the_geom.centroid.x,
                         e.destination.border.the_geom.centroid.y]
            yr = Date.objects.get(year=year)
            lyr['data'].append({"from": origPoint, "to": destPoint,
                                "labels": ["", e.destination.name +
                                           " " + str(e.recognisedrate.
                                                     __float__())],
                                "color": "#333333"})
            migLayers.append(lyr)
    return JsonResponse(lyr, safe=False)
