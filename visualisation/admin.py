from django.contrib import admin


from visualisation.models import (Country, Date, MigrationEvent)

admin.site.register(Country)
admin.site.register(Date)
admin.site.register(MigrationEvent)
