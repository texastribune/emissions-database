from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from emissions.models import EmissionEvent, ContaminantReleased, RequestAttempt, REPermit, IssuedOrder
from emissions.views import search_view, regulated_entity_view, county_view
from infoNavigator.views import RecordsView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^search/', search_view),
    url(r'^regulated-entity/(?P<pk>\d+)/', regulated_entity_view, name=u'entity_detail'),
    url(r'^county/(?P<county_name>\w+)/', county_view, name=u'county_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'navigate/', RecordsView(EmissionEvent, ContaminantReleased, RequestAttempt,
                                  REPermit, IssuedOrder).as_view())
)
