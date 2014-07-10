# isles/urls.py
from __future__ import absolute_import
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    # List all isles
    #url(r'^$', views.Index.as_view(), name='index'),
    #
    # /isles/create/ -- Add a new store
    #url(r'^create/$', views.IsleCreateView.as_view(), name='create'),
    #
    # /isles/<slug>/
    #url(r'^(?P<slug>[\w-]+)/$',         views.IsleDetailView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/update/$',  views.IsleUpdateView.as_view(), name='update'),
)
