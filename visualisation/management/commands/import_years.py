from django.core.management import BaseCommand
import csv

from visualisation.models import Date


class Command(BaseCommand):
    help = 'Imports years into the database from the Neymayer CSV.\
            \n \n Usage: import_years /path/to/file.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_path')

    def handle(self, *args, **options):

        # Define arguments
        csv_path = options['csv_path']

        # Open csv file
        try:
            with open(csv_path, 'rb') as csv_file:

                year_list = []

                reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                for row in reader:
                    # Year is in column 33
                    if not row[33] in year_list:
                        year_list.append(row[33])

                for year in year_list:
                    if not Date.objects.filter(year=year).count():
                        date = Date()
                        date.year = year
                        date.save()
                        print '{} added to the database'.format(year)
                    else:
                        print '{} not added - already in the database'.format(
                            year)

        except Exception, e:
            print "An error occured - caught Exception"
            print e
