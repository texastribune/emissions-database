from django.conf.urls import patterns, include, url
# from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'emission_events.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the import above and next line to serve media files in development
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
