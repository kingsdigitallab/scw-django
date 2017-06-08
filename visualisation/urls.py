from django.conf.urls import url

from visualisation.views import mapview, mapCountry

urlpatterns = [
    url(r'^map/(\d+)', mapCountry, name='map_country'),
    url(r'^map/$', mapview, name='map_view'),
    # url(r'^modules/(?P<pk>\d+)/$', module_detail, name='module_detail'),
]
