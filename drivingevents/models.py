from __future__ import unicode_literals

from django.db import models


# Driving Events
class DrivingEvent(models.Model):
    name = models.CharField(verbose_name="Event Name", max_length=128,
                            blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Driving Event'
        verbose_name_plural = 'Driving Events'


# Duration Type (Weeks...)
class DurationType(models.Model):
    name = models.CharField(verbose_name="Duration Type", max_length=256,
                            blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Duration Type'
        verbose_name_plural = 'Duration Types'


# Location (Abstracted for future dev)
class Location(models.Model):
    name = models.CharField(verbose_name="Location Name", max_length=128,
                            blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


# Organisation
class Organisation(models.Model):
    name = models.CharField(verbose_name="Organisation", max_length=256,
                            blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'


# Political Views (L/R...)
class PoliticalView(models.Model):
    name = models.CharField(verbose_name="Political View", max_length=128,
                            blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Political View'
        verbose_name_plural = 'Political Views'


# Transport Type
class TransportType(models.Model):
    name = models.CharField(verbose_name="Transport Type", max_length=256,
                            blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Transport Type'
        verbose_name_plural = 'Transport Types'


# Migration Event Definition
class MigrationEvent(models.Model):
    name = models.CharField(verbose_name="Name", max_length=128,
                            blank=True)

    # Year
    date_y = models.IntegerField(verbose_name="Year", blank=False,)
    # From Month
    date_m_from = models.IntegerField(verbose_name="From (Month)", blank=True,
                                      null=True)

    # To Month
    date_m_to = models.IntegerField(verbose_name="To (Month)", blank=True,
                                    null=True)

    # Date Uncertain
    date_uncertain = models.BooleanField(verbose_name="Uncertain Date?",
                                         blank=False, default=False)

    # Original Date String
    date_str = models.TextField(verbose_name="Date Notes", blank=False)

    # Left or Right
    political_view = models.ForeignKey(PoliticalView, null=True,
                                       verbose_name="Political View")

    # Who? For now we're storing as a string,
    # then we'll process later after cleaning
    who_str = models.TextField(verbose_name="Who (Text)", blank=True)

    # Counts:
    count_children = models.IntegerField(verbose_name="Child Count",
                                         blank=False)

    count_adults = models.IntegerField(verbose_name="Adult Count",
                                       blank=False)

    count_uncertain = models.BooleanField(verbose_name="Uncertain Counts?",
                                          blank=False, default=False)

    # Driving Events:
    driving_events = models.ManyToManyField(DrivingEvent, blank=True)

    # Locations:
    location_from = models.ForeignKey(Location, blank=True, null=True,
                                      verbose_name="From (Location)",
                                      related_name="location_from")
    location_to = models.ForeignKey(Location, blank=True, null=True,
                                    verbose_name="To (Location)",
                                    related_name="location_to")

    # Transport:
    transport_types = models.\
        ManyToManyField(TransportType, blank=True,
                        verbose_name="Transport Types",
                        related_name="transport_types")

    transport_desc = models.TextField(verbose_name="Description of Transport",
                                      blank=True)

    transport_organisers = models.\
        ManyToManyField(Organisation, blank=True,
                        verbose_name="Transport Organisers",
                        related_name="transport_organisers")

    # Length of stay info:
    length_of_stay_desc = models.TextField(verbose_name="Description of\
                                           length of stay", blank=True)

    length_of_stay_type = models.ForeignKey(DurationType, blank=True,
                                            null=True,
                                            verbose_name="Length of Stay")

    # Carers
    cared_by = models.TextField(verbose_name="Cared For By",
                                blank=True)

    caregivers = models.ManyToManyField(Organisation, blank=True,
                                        verbose_name="Caregivers",
                                        related_name="caregivers")

    # Source
    source = models.TextField(verbose_name="Source", blank=True)

    def count(self):
        return self.count_adults + self.count_children

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Migration Event'
        verbose_name_plural = 'Migration Events'
