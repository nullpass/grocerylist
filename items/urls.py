# items/urls.py
from __future__ import absolute_import
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    # List all item
    #url(r'^$', views.Index.as_view(), name='index'),
    #
    # /item/create/ -- Add a new store
    #url(r'^create/$', views.ItemCreateView.as_view(), name='create'),
    #
    # /item/<slug>/
    #url(r'^(?P<slug>[\w-]+)/$',         views.ItemDetailView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/update/$',  views.ItemUpdateView.as_view(), name='update'),
)
