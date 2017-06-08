from django.shortcuts import render

# from visualisation.models import MigrationEvent
# from haystack.query import SearchQuerySet
# from haystack.inputs import AutoQuery


# Department view
def mapview(request):
    context = {
        'test': 'test',
    }
    return render(request, 'visualisation/map.html', context)

# Commented out to stop flake8 moanint - no views yet!
# from django.shortcuts import render
