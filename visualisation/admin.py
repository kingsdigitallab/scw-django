from django.contrib.gis import admin

from visualisation.models import (Country, Date, MigrationEvent, WorldBorders)


class WorldBordersAdmin(admin.OSMGeoAdmin):
    openlayers_url = 'https://openlayers.org/api/2.13.1/OpenLayers.js'


admin.site.register(Country)
admin.site.register(Date)
admin.site.register(MigrationEvent)
admin.site.register(WorldBorders, WorldBordersAdmin)
