from django.contrib import admin

from drivingevents.models import (DrivingEvent, DurationType, Location,
                                  Organisation, PoliticalView, TransportType,
                                  MigrationEvent)
# Register your models here.
admin.site.register(DrivingEvent)
admin.site.register(DurationType)
admin.site.register(Location)
admin.site.register(Organisation)
admin.site.register(PoliticalView)
admin.site.register(TransportType)
admin.site.register(MigrationEvent)
