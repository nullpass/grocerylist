# stores/urls.py
from __future__ import absolute_import
from django.conf.urls import patterns, include, url

from isles.views import IsleDetailView, IsleUpdateView, IsleCreateView
from items.views import ItemCreateView

from . import views

"""
item_patterns = patterns('',
    #
    # /s/<store slug>/<isle id>/<item slug>/
    url(r'^$',         ItemDetailView.as_view(), name='detail'),
    #
    # /s/<store slug>/<isle id>/<item slug>/update
    url(r'^update/$',  ItemUpdateView.as_view(), name='update'),
)
"""

isle_patterns = patterns('',
    #
    # /s/<store slug>/<isle id>/
    url(r'^$',         IsleDetailView.as_view(), name='detail'),
    #
    # /s/<store slug>/<isle id>/update
    url(r'^update/$',  IsleUpdateView.as_view(), name='update'),
    #
    # /s/<store slug>/<isle id>/update
    url(r'^create/$',  IsleCreateView.as_view(), name='create'),
    #
    # /s/<store slug>/<isle id>/<item slug>
    # url(r'^(?P<slug>[\w-]+)/', include(item_patterns, namespace='item')),
)

urlpatterns = patterns('',
    #
    # /s/<store slug>/
    url(r'^$',         views.StoreDetailView.as_view(), name='detail'),
    #
    # /s/<store slug>/update/    
    url(r'^update/$',  views.StoreUpdateView.as_view(), name='update'),
    #
    # /s/<store slug>/<isle id>/
    url(r'^(?P<pk>[\d]+)/', include(isle_patterns, namespace='isle')),
    #
    # /s/<store slug>/isle-create/
    url(r'^isle/create/$',  IsleCreateView.as_view(), name='isle-create'),
    #
    # /s/<store slug>/item-create/
    url(r'^item/create/$',  ItemCreateView.as_view(), name='item-create'),
)
