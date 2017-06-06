from django.core.management import BaseCommand
import csv

from drivingevents.models import (DrivingEvent, DurationType, Location,
                                  Organisation, PoliticalView, TransportType,
                                  MigrationEvent)


class Command(BaseCommand):
    help = 'Imports driving events data\
            \n \n Usage: import_driving_events /path/to/file.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_path')

    def handle(self, *args, **options):

        # Define arguments
        csv_path = options['csv_path']

        # Open csv file
        with open(csv_path, 'rb') as csv_file:

            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for row in reader:
                # Create Migration Event
                me = MigrationEvent()

                # Year: col 0
                me.date_y = int(row[0])

                # Month From/To: cols 1/2
                if not row[1] == "":
                    me.date_m_from = int(row[1])

                if not row[2] == "":
                    me.date_m_to = int(row[2])

                # Uncertain Date? col 3
                if row[2].upper() == "Y":
                    me.date_uncertain = True
                else:
                    me.date_uncertain = False

                # Date String (original) col 4
                me.date_str = row[4]

                # Political View col 6:
                obj_pol = PoliticalView.objects.filter(
                    name=row[6]).all()

                if len(obj_pol):
                    me.political_view = obj_pol[0]
                else:
                    obj_pol = PoliticalView()
                    obj_pol.name = row[6]
                    obj_pol.save()
                    me.political_view = obj_pol

                # Name. col 7:
                me.name = row[7]

                # Who (text string, col 8)
                me.who_str = row[8]

                # Counts (cols 9/10)
                if row[9] == "":
                    me.count_children = 0
                else:
                    me.count_children = int(row[9])

                if row[10] == "":
                    me.count_adults = 0
                else:
                    try:
                        me.count_adults = int(row[10])
                    except:
                        me.count_adults = int(row[11])

                # Uncertain count? col 12
                if row[12].upper() == "Y":
                    me.count_uncertain = True
                else:
                    me.count_uncertain = False

                # Locations
                # From (col 14)
                if not row[14] == "":
                    obj_loc = Location.objects.filter(
                        name=row[14]).all()
                    if len(obj_loc):
                        me.location_from = obj_loc[0]
                    else:
                        obj_loc = Location()
                        obj_loc.name = row[14]
                        obj_loc.save()
                        me.location_from = obj_loc

                # To (col 15)
                if not row[15] == "":
                    obj_loc = Location.objects.filter(
                        name=row[15])
                    if obj_loc.count():
                        me.location_to = obj_loc[0]
                    else:
                        obj_loc = Location()
                        obj_loc.name = row[15]
                        obj_loc.save()
                        me.location_to = obj_loc

                # Transport Description (col 16)
                me.transport_desc = row[16]

                # Length of stay desc (col 19)
                me.length_of_stay_desc = row[19]

                # length of stay type (col 20)
                if not row[20] == "":
                    obj_dur = DurationType.objects.filter(
                        name=row[20]).all()
                    if len(obj_dur):
                        me.length_of_stay_type = obj_dur[0]
                    else:
                        obj_dur = DurationType()
                        obj_dur.name = row[20]
                        obj_dur.save()

                        me.length_of_stay_type = obj_dur

                # cared_by (col 21)
                me.cared_by = row[21]

                # source
                me.source = row[23]

                me.save()

                # After save:

                # Driving Events - col 13 M2M
                if not row[13] == "":
                    for event in row[13].split(","):
                        drv_obj = DrivingEvent.objects.filter(
                            name=event).all()
                        if len(drv_obj):
                            me.driving_events.add(drv_obj[0])
                        else:
                            drv_obj = DrivingEvent()
                            drv_obj.name = event
                            drv_obj.save()
                            me.driving_events.add(drv_obj)

                # Transport type (col 17), M2M comma split
                if not row[17] == "":
                    for trans in row[17].split(","):
                        trans_obj = TransportType.objects.filter(
                            name=trans).all()
                        if len(trans_obj):
                            me.transport_types.add(trans_obj[0])
                        else:
                            trans_obj = TransportType()
                            trans_obj.name = trans
                            trans_obj.save()
                            me.transport_types.add(trans_obj)

                # Transport organisers (col 18), m2m comma split
                if not row[18] == "":
                    for org in row[18].split(","):
                        org_obj = Organisation.objects.filter(
                            name=org).all()
                        if len(org_obj):
                            me.transport_organisers.add(org_obj[0])
                        else:
                            org_obj = Organisation()
                            org_obj.name = org
                            org_obj.save()
                            me.transport_organisers.add(org_obj)

                # caregivers (col 22, M2M comma seperated)
                if not row[22] == "":
                    for org in row[22].split(","):
                        org_obj = Organisation.objects.filter(
                            name=org).all()
                        if len(org_obj):
                            me.caregivers.add(org_obj[0])
                        else:
                            org_obj = Organisation()
                            org_obj.name = org
                            org_obj.save()
                            me.caregivers.add(org_obj)
