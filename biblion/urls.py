# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r'^$', "biblion.views.blog_index", name="blog"),
    
    url(u'^search/$', "biblion.views.blog_search", name="blog-search"),
    url(u'^search/(?P<keyword>[\w\W\d\-\+\s_]+)/$', "biblion.views.blog_search", name="blog-search"),
    
    url(r'^tag/(?P<tagname>[\w\d\-_]+)/$', "biblion.views.blog_by_tag", name="blog-tags"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', "biblion.views.blog_post_detail", name="blog_post"),
    url(r'^post/(?P<post_pk>\d+)/$', "biblion.views.blog_post_detail", name="blog_post_pk"),
    url(r'^(?P<section>[-\w]+)/$', "biblion.views.blog_section_list", name="blog_section"),
)
