from django.contrib import admin
from emissions.models import PageHTML, EmissionEvent, RequestAttempt,\
                            ContaminantReleased


class EmissionEventAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'county', 'began_date']
    fieldsets = [
        ('Tracking Number', {'fields': ['tracking_number']}),
        ('Curated', {'fields': [
            'county',
            'city',
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

class ContaminantReleasedAdmin(admin.ModelAdmin):
    list_display = ['contaminant_parameterized', 'tracking_number']
    fieldsets = [
        ('Curated', {'fields': [
            'contaminant_parameterized',
            'limit_lbs',
            'amount_released_lbs',
            'tracking_number'
            ]}),
        ('HTML', {'fields': [
            'contaminant',
            'authorization',
            'limit',
            'amount_released'
            ]})
    ]

class PageHTMLAdmin(admin.ModelAdmin):
    list_display = ['tracking_number']


admin.site.register(PageHTML, PageHTMLAdmin)
admin.site.register(EmissionEvent, EmissionEventAdmin)
admin.site.register(RequestAttempt)
admin.site.register(ContaminantReleased, ContaminantReleasedAdmin)
