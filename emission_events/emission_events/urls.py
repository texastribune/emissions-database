from django.conf.urls import patterns, include, url
from emissions.views import home
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
)
