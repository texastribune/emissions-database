from django.db import models

class EmissionEvent(models.Model):
    tracking_number = models.IntegerField(null=False,unique=True)
    # Regulated entity name
    regulated_entity_name = models.CharField(max_length=200)
    # Physical location
    physical_location = models.TextField()
    # Regulated entity RN number
    regulated_entity_rn_number = models.CharField(max_length=200)
    # City, County
    city_county = models.CharField(max_length=200)
    # Type(s) of air emissions event:
    type_of_air_emissions_event = models.CharField(max_length=200)
    # This is based on the:
    based_on_the = models.CharField(max_length=200)
    # Event began:
    event_began = models.CharField(max_length=200)
    # Event ended:
    event_ended = models.CharField(max_length=200)
    # Cause
    cause = models.TextField()
    # Action taken
    action_taken = models.TextField()
    # Emissions estimation method
    emissions_estimation_method = models.TextField()


class PageHTML(models.Model):
    tracking_number = models.IntegerField(null=False,unique=True)
    content         = models.TextField()


class RequestAttempt(models.Model):
    tracking_number = models.IntegerField(null=False,unique=True)
    request_date = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=200)
    status_code = models.CharField(max_length=200)
    failed = models.BooleanField(default=False)
