from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', 'direct_to_template', {'template':'index.xhtml'}, "pugce-index"),
)
