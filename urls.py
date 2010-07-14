from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^admin/', include(admin.site.urls)),
    (r'^', include('pugce.website.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns( '',
        ( r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$',\
            'django.views.static.serve', \
            { 'document_root': settings.MEDIA_ROOT, 'show_indexes': False } )
    )
