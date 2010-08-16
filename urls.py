from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^coord/', include(admin.site.urls)),
    (r'^blog/', include('pugce.biblion.urls')),
    (r'^wiki/', include('pugce.wiki.urls')),
    (r'^', include('pugce.website.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns( '',
        ( r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$',\
            'django.views.static.serve', \
            { 'document_root': settings.MEDIA_ROOT, 'show_indexes': False })
    )
