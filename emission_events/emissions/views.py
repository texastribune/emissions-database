from django.http import Http404, HttpResponse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from models import RegulatedEntity

# validate len(q) > 2

def search_view(request):
    regulated_entities = RegulatedEntity.objects.filter(\
        Q(name__icontains=request.GET['q']) |\
        Q(county__icontains=request.GET['q']) |\
        Q(nearest_city__icontains=request.GET['q']) |\
        Q(regulated_entity_rn_number__icontains=request.GET['q']))

    return render(request, 'search.html', {
        'q': request.GET['q'],
        'regulated_entities': regulated_entities
    })


def regulated_entity_view(request, pk):
    regulated_entity = get_object_or_404(RegulatedEntity, pk=pk)

    return render(request, 'regulated_entity.html', {
        'regulated_entity': regulated_entity
    })
