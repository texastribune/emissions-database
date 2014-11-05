from django.db import models


class PageHTML(models.Model):
    tracking_number = models.IntegerField(null=False,unique=True)
    content         = models.TextField()


class EmissionEvent(models.Model):
    tracking_number = models.IntegerField(null=False,unique=True)
    dc_date_meta = models.CharField(max_length=20, null=True)
    # Regulated entity name
    regulated_entity_name = models.CharField(max_length=30)
    # Physical location
    physical_location = models.TextField()
    # Regulated entity RN number
    regulated_entity_rn_number = models.CharField(max_length=50)
    # City, County
    city_county = models.CharField(max_length=50)
    # Type(s) of air emissions event:
    type_of_air_emissions_event = models.CharField(max_length=200)
    # This is based on the:
    based_on_the = models.CharField(max_length=50)
    # Event began:
    event_began = models.CharField(max_length=30)
    # Event ended:
    event_ended = models.CharField(max_length=30)
    # Cause
    cause = models.TextField()
    # Action taken
    action_taken = models.TextField()
    # Emissions estimation method
    emissions_estimation_method = models.TextField()

    # Curated fields
    dc_date = models.DateField(null=True)
    city = models.CharField(max_length=200, db_index=True, null=True)
    county = models.CharField(max_length=200, db_index=True, null=True)
    began_date = models.DateTimeField(db_index=True, null=True)
    ended_date = models.DateTimeField(db_index=True, null=True)
    duration = models.FloatField(null=True) # in hours
    type_of_emission = models.CharField(max_length=30, db_index=True)

    # Relations
    page_html = models.ForeignKey(PageHTML)
    regulated_entity = models.ForeignKey(RegulatedEntity)


class ContaminantReleased(models.Model):
    tracking_number = models.IntegerField(null=False)

    # Relations
    emission_event = models.ForeignKey(EmissionEvent)

    # Original values
    contaminant = models.CharField(max_length=100)
    authorization = models.CharField(max_length=200)
    limit = models.CharField(max_length=100)
    amount_released = models.CharField(max_length=200)

    # Curated fields
    contaminant_parameterized = models.CharField(max_length=100, db_index=True)
    limit_lbs = models.FloatField(null=True)
    amount_released_lbs = models.FloatField(null=True)
    limit_op = models.FloatField(null=True)
    amount_released_op = models.FloatField(null=True)


class RequestAttempt(models.Model):
    tracking_number = models.IntegerField(null=False)
    request_date = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=200)
    status_code = models.CharField(max_length=200)
    failed = models.BooleanField(default=False)


class RegulatedEntity(models.Model):
    url = models.CharField(max_length=200)
    regulated_entity_rn_number = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    primary_business = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    county = models.CharField(max_length=30)
    nearest_city = models.CharField(max_length=30)
    nearest_zipcode = models.CharField(max_length=30)
    physical_location = models.CharField(max_length=200)


class REPermit(models.Model):
    program = models.CharField(max_length=100)
    id_type = models.CharField(max_length=30)
    id_number = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    url = models.CharField(max_length=100)

    # Flags
    proposed_enforcement_orders = models.BooleanField(default=False)
    effective_enforcement_orders = models.BooleanField(default=False)
    notice_of_violations = models.BooleanField(default=False)

    # Relations
    regulated_entity = models.ForeignKey(RegulatedEntity)

