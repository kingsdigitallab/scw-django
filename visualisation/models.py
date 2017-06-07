from __future__ import unicode_literals

from django.contrib.gis.db import models


class WorldBorders(models.Model):
    gid = models.AutoField(primary_key=True)
    fips = models.CharField(max_length=2, blank=True, null=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    un = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    pop2005 = models.DecimalField(max_digits=10, decimal_places=0,
                                  blank=True, null=True)
    region = models.SmallIntegerField(blank=True, null=True)
    subregion = models.SmallIntegerField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    the_geom = models.GeometryField(blank=True, null=True,
                                    srid=4326)

    class Meta:
        managed = False
        db_table = 'tm_world_borders'

    def __unicode__(self):
        return self.name


# Defines a country
class Country(models.Model):
    name = models.CharField(verbose_name="Country", max_length=128,
                            blank=False)
    border = models.ForeignKey(WorldBorders, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


# To allow extension in the future
class Date(models.Model):
    day = models.IntegerField(blank=True, null=True, help_text="If Known")
    month = models.IntegerField(blank=True, null=True, help_text="If Known")
    year = models.IntegerField(blank=False, null=False)

    def __unicode__(self):
        if self.day and self.month:
            return '{}/{}/{}'.format(self.day, self.month, self.year)
        elif self.month:
            return '{}/{}'.format(self.month, self.year)
        else:
            return str(self.year)

    class Meta:
        ordering = ['year', 'month', 'day']
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'


# Migration Event
class MigrationEvent(models.Model):
    approvalrate = models.DecimalField(max_digits=20, decimal_places=15,
                                       null=True, blank=True)
    date = models.ForeignKey(Date, verbose_name='Date', help_text='Can input\
                             just year if full date is unknown')
    destination_unemployment = models.DecimalField(max_digits=20,
                                                   decimal_places=15,
                                                   verbose_name='Destination\
                                                   Unemployment', null=True,
                                                   blank=True)
    destination_gdp = models.DecimalField(max_digits=20, decimal_places=15,
                                          verbose_name='Destination\
                                          GDP Per Capita', null=True,
                                          blank=True)
    destination_rwpvote = models.DecimalField(max_digits=20,
                                              decimal_places=15,
                                              help_text='Meaning\
                                              unknown', null=True, blank=True)
    destination = models.ForeignKey(Country, related_name='destination')
    euplusasyl = models.IntegerField(help_text='Meaning unknown', null=True,
                                     blank=True)
    free = models.DecimalField(max_digits=20, decimal_places=15,
                               help_text='Sum of the two Freedom House\
                               indices of political rights and civil\
                               liberties, each ranging from 1(most\
                               to 7 (least free) (AUTOCRACY)', null=True,
                               blank=True)
    genpoliticidemag = models.DecimalField(max_digits=20, decimal_places=15,
                                           help_text='Magnitude score for\
                                           number of deaths from genocide\
                                           and politicide (GEN/POLITICIDE)',
                                           null=True, blank=True)
    l52dyadasylumcorrpc = models.DecimalField(max_digits=20, decimal_places=15,
                                              help_text='Meaning\
                                              unknown', null=True, blank=True)
    l52dyadasylumtotalpc = models.DecimalField(max_digits=20,
                                               decimal_places=15,
                                               help_text='Meaning\
                                               unknown', null=True, blank=True)
    origin = models.ForeignKey(Country, related_name='origin')
    origin_gdp = models.DecimalField(max_digits=20, decimal_places=15,
                                     verbose_name='Origin GDP Per Capita',
                                     null=True, blank=True)
    pts = models.DecimalField(max_digits=20, decimal_places=15,
                              help_text='average of two Political Terror\
                              Scales measuring human rights violations,\
                              ranging from 1 (best) to 5 (worst)', null=True,
                              blank=True)
    recognisedrate = models.DecimalField(max_digits=20, decimal_places=15,
                                         null=True, blank=True)
    sfallmax = models.DecimalField(max_digits=20, decimal_places=15,
                                   help_text='Magnitude score for civil\
                                   war, ethnic war, or collapse of state\
                                   authority (DOMWAR/STATEFAIL)', null=True,
                                   blank=True)
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
                                                   year)', null=True,
                                                   blank=True)

    def __unicode__(self):
        return 'From {} To {} in {}'.format(self.origin.name,
                                            self.destination.name,
                                            self.date.year)

    class Meta:
        ordering = ['origin__name', 'destination__name', 'date__year']
        verbose_name = 'Migration Event'
        verbose_name_plural = 'Migration Events'
