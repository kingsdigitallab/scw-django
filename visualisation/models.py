from __future__ import unicode_literals

from django.db import models


# Defines a country
class Country(models.Model):
    name = models.CharField(verbose_name="Country", max_length=128,
                            blank=False)


# To allow extension in the future
class Date(models.Model):
    day = models.IntegerField(blank=True, help_text="If Known")
    month = models.IntegerField(blank=True, help_text="If Known")
    year = models.IntegerField(blank=False)


# Migration Event
class MigrationEvent(models.Model):
    approvalrate = models.DecimalField(max_digits=20, decimal_places=15)
    date = models.ForeignKey(Date, verbose_name='Date', help_text='Can input\
                             just year if full date is unknown')
    destination_unemployment = models.DecimalField(max_digits=20,
                                                   decimal_places=15,
                                                   verbose_name='Destination\
                                                   Unemployment')
    destination_gdp = models.DecimalField(max_digits=20, decimal_places=15,
                                          verbose_name='Destination\
                                          GDP Per Capita')
    destination_rwpvote = models.DecimalField(max_digits=20, decimal_places=15,
                                              help_text='Meaning\
                                              unknown')
    destination = models.ForeignKey(Country, related_name='destination')
    euplusasyl = models.IntegerField(help_text='Meaning unknown')
    free = models.IntegerField(help_text='Sum of the two Freedom House\
                               indices of political rights and civil\
                               liberties, each ranging from 1 (most free)\
                               to 7 (least free) (AUTOCRACY)')
    genpoliticidemag = models.DecimalField(max_digits=20, decimal_places=15,
                                           help_text='Magnitude score for\
                                           number of deaths from genocide\
                                           and politicide (GEN/POLITICIDE)')
    l52dyadasylumcorrpc = models.DecimalField(max_digits=20, decimal_places=15,
                                              help_text='Meaning\
                                              unknown')
    l52dyadasylumtotalpc = models.DecimalField(max_digits=20,
                                               decimal_places=15,
                                               help_text='Meaning\
                                               unknown')
    origin = models.ForeignKey(Country, related_name='origin')
    origin_gdp = models.DecimalField(max_digits=20, decimal_places=15,
                                     verbose_name='Origin GDP Per Capita')
    pts = models.DecimalField(max_digits=20, decimal_places=15,
                              help_text='average of two Political Terror\
                              Scales measuring human rights violations,\
                              ranging from 1 (best) to 5 (worst)')
    recognisedrate = models.DecimalField(max_digits=20, decimal_places=15)
    sfallmax = models.DecimalField(max_digits=20, decimal_places=15,
                                   help_text='Magnitude score for civil\
                                   war, ethnic war, or collapse of state\
                                   authority (DOMWAR/STATEFAIL)')
    uppsalaexternalintensity = models.IntegerField(help_text='Intensity of\
                                                   external conflicts, on an\
                                                   ordered categorical scale\
                                                   (0 = no conflict, 1 =\
                                                   25-999 deaths that year in\
                                                   minor conflict, 2 = 25-999\
                                                   deaths that year in\
                                                   conflict totaling 1000+\
                                                   deaths across years,\
                                                   3 = 1000+ deaths that\
                                                   year)')
