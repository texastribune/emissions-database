from import_export import resources
from models import ContaminantReleased, EmissionEvent


class ContaminantResource(resources.ModelResource):
    class Meta:
        model = ContaminantReleased


class EmissionResource(resources.ModelResource):
    class Meta:
        model = EmissionEvent
