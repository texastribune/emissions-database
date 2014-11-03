from django.contrib import admin
from emissions.models import PageHTML, EmissionEvent, RequestAttempt,\
                            ContaminantReleased


class EmissionEventAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'type_of_emission', 'duration', 'county']
    list_filter = ['type_of_emission', 'county']
    fieldsets = [
        ('Tracking Number', {'fields': ['tracking_number']}),
        ('Curated', {'fields': [
            'county',
            'city',
            'type_of_emission',
            'dc_date',
            'began_date',
            'ended_date',
            'duration',
            ]}),
        ('HTML', {'fields': ['dc_date_meta',
                                'regulated_entity_name',
                                'physical_location',
                                'regulated_entity_rn_number',
                                'city_county',
                                'type_of_air_emissions_event',
                                'based_on_the',
                                'event_began',
                                'event_ended',
                                'cause',
                                'action_taken',
                                'emissions_estimation_method'
            ]})
    ]
    ordening = 'tracking_number'

class ContaminantReleasedAdmin(admin.ModelAdmin):
    list_display = ['contaminant_parameterized', 'tracking_number', 'amount_released_lbs']
    list_filter = ['contaminant_parameterized']
    fieldsets = [
        ('Curated', {'fields': [
            'contaminant_parameterized',
            'limit_lbs',
            'limit_op',
            'amount_released_lbs',
            'amount_released_op',
            'tracking_number'
            ]}),
        ('HTML', {'fields': [
            'contaminant',
            'authorization',
            'limit',
            'amount_released'
            ]})
    ]
    ordening = 'tracking_number'

class PageHTMLAdmin(admin.ModelAdmin):
    list_display = ['tracking_number']
    ordening = 'tracking_number'

class RequestAttemptAdmin(admin.ModelAdmin):
    list_display = ['tracking_number']
    ordening = 'tracking_number'


admin.site.register(PageHTML, PageHTMLAdmin)
admin.site.register(EmissionEvent, EmissionEventAdmin)
admin.site.register(RequestAttempt, RequestAttemptAdmin)
admin.site.register(ContaminantReleased, ContaminantReleasedAdmin)
