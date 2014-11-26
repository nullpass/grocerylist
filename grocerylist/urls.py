# grocerylist/urls.py
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from lists.views import ListCreateView, ListUpdateView, ListDetailView, ListIndex

from items.views import ItemCreateView, ItemUpdateView, ItemIndex

from isles.views import IsleCreateView, IsleUpdateView

from stores.views import StoreCreateView, StoreDetailView, StoreUpdateView, StoreIndex

from recent.views import RecentDetailView, RecentIndex

from core.views import LogoutView, HelpView

item_patterns = patterns('',
    #
    # /i/<item pk>/update/
    url(r'^(?P<pk>\d+)/update/$', ItemUpdateView.as_view(), name='update'),
)

isle_patterns = patterns('',
    #
    # /s/<store slug>/<isle id>/update
    url(r'^update/$',  IsleUpdateView.as_view(), name='update'),
)

store_patterns = patterns('',
    #
    # /s/<store slug>/
    url(r'^$',         StoreDetailView.as_view(), name='detail'),
    #
    #
    url(r'^inventory/$',   ItemIndex.as_view(), name='inventory'),
    #
    # /s/<store slug>/generate/
    url(r'^generate/$',   ListCreateView.as_view(), name='generate'),
    #
    # /s/<store slug>/update/    
    url(r'^update/$',  StoreUpdateView.as_view(), name='update'),
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

mylist_patterns = patterns('',
    #
    # /mylists/
    url(r'^$', ListIndex.as_view(), name='index'),
    #
    # /mylists/<item pk>/
    url(r'^(?P<pk>\d+)/$', ListDetailView.as_view(), name='detail'),
    #
    # /mylists/<item pk>/update/
    url(r'^(?P<pk>\d+)/update/$', ListUpdateView.as_view(), name='update'),
)

recent_patterns = patterns('',
    #
    # /recent/
    url(r'^$', RecentIndex.as_view(), name='index'),  ## Wait-- why the hell did I insist on a single urls file??
    #
    # /recent/<log pk>/
    url(r'^(?P<pk>\d+)/$', RecentDetailView.as_view(), name='detail'),
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #
    # /
    url(r'^$', StoreIndex.as_view(), name='index'),
    #
    # 
    url(r'^auth3p$', TemplateView.as_view(template_name='auth3p.html'), name='auth3p'), # Choose your auth, Twitter/Google/Etc
    url(r'^logout$', LogoutView.as_view(), name='logout'), 
    #
    # Dynamic help view
    url(r'/help/$', HelpView.as_view(), name='help'), #  http://hostname/x/y-z/help/
    url(r'^help/$', HelpView.as_view(), name='help'), #  http://hostname/help/
    #
    # /create/ 
    url(r'^create/', StoreCreateView.as_view(), name='create'),
    #
    # /s/<store slug>/
    url(r'^s/(?P<slug>[\w-]+)/', include(store_patterns,   namespace='stores')),
    #
    # /mylists/
    url(r'^mylists/', include(mylist_patterns, namespace='lists')),
    #
    # /i/
    url(r'^i/', include(item_patterns, namespace='items')),
    #
    # /recent/ 
    url(r'^recent/', include(recent_patterns, namespace='recent')),
    #
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
