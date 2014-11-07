from django.db.models import Q
from django.shortcuts import render
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
