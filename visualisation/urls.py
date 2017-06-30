from django.conf.urls import url

from visualisation.views import mapview, mapCountry, migrationLayer, \
    countryUpdate

urlpatterns = [
    url(r'^map/(\d+)/(\d+)/$', migrationLayer, name='migration_layer'),
    url(r'^map/(\d+)', mapCountry, name='map_country'),
    url(r'^map/$', mapview, name='map_view'),
    url(r'^country/$', countryUpdate, name='country_update')
]
