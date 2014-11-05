from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from emissions.views import search


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^search/', search),
    url(r'^admin/', include(admin.site.urls)),
)
