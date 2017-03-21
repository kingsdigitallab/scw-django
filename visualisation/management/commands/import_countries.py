from django.core.management import BaseCommand
import csv

from visualisation.models import Country


class Command(BaseCommand):
    help = 'Imports countries into the database from the Neymayer CSV.\
            \n \n Usage: import_countries /path/to/file.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_path')

    def handle(self, *args, **options):

        # Define arguments
        csv_path = options['csv_path']

        # Open csv file
        try:
            with open(csv_path, 'rb') as csv_file:

                country_list = []

                reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                for row in reader:

                    # To/From Countries are in columns 32 and 34
                    if not row[32] in country_list:
                        country_list.append(row[32])

                    if not row[34] in country_list:
                        country_list.append(row[34])

                for country in country_list:
                    if not Country.objects.filter(name=country).count():
                        obj = Country()
                        obj.name = country
                        obj.save()
                        print '{} added to the database'.format(country)
                    else:
                        print '{} not added - already in the database'.format(
                            country)

        except Exception, e:
            print "An error occured - caught Exception"
            print e
