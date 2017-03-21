from django.core.management import BaseCommand
import csv

from visualisation.models import Country, Date, MigrationEvent


class Command(BaseCommand):
    help = 'Imports migration events into the database from the\
            Neymayer CSV.\
            \n \n Usage: import_events /path/to/file.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_path')

    def handle(self, *args, **options):

        # Define arguments
        csv_path = options['csv_path']

        # Open csv file
        try:
            with open(csv_path, 'rb') as csv_file:

                reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                for row in reader:

                    # OK, we have lots of columns to deal with here.
                    # Need to be careful!
                    me = MigrationEvent()

                    # Doing this in the order of data on the spreadsheet
                    if row[0]:
                        me.destination_unemployment = row[0]
                    # Row 1 unused (Country ID)
                    if row[2]:
                        # data cleansing!
                        me.free = row[2]
                    if row[3]:
                        me.genpoliticidemag = row[3]
                    if row[4]:
                        me.origin_gdp = row[4]
                    if row[5]:
                        me.pts = row[5]
                    if row[6]:
                        me.sfallmax = row[6]
                    if row[7]:
                        me.uppsalaexternalintensity = row[7]
                    if row[8]:
                        me.euplusasyl = row[8]
                    if row[9]:
                        me.destination_gdp = row[9]
                    if row[10]:
                        me.destination_rwpvote = row[10]
                    if row[11]:
                        me.approvalrate = row[11]
                    if row[12]:
                        me.recognisedrate = row[12]
                    # Rows 13-29 are country IDs
                    if row[30]:
                        me.l52dyadasylumcorrpc = row[30]
                    if row[31]:
                        me.l52dyadasylumtotalpc = row[31]

                    # Get origin (32) and destination (34) countries
                    me.origin = Country.objects.get(name=row[32])
                    me.destination = Country.objects.get(name=row[34])

                    # Get Date (year (33) only obviously)
                    me.date = Date.objects.get(year=row[33])

                    # And Breathe (save)
                    me.save()

                    # Output to console for sanity:
                    print 'Added event: {}'.format(me)

        except Exception, e:
            print "An error occured - caught Exception"
            print e
