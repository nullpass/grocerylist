# grocerylist/urls.py
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from isles.view.create import do as IsleCreateView
from isles.view.delete import do as IsleDeleteView
from isles.view.update import do as IsleUpdateView

from items.view.create import do as ItemCreateView
from items.view.delete import do as ItemDeleteView
from items.view.index  import do as ItemIndex
from items.view.update import do as ItemUpdateView

from lists.view.create import do as ListCreateView
from lists.view.delete import do as ListDeleteView
from lists.view.detail import do as ListDetailView
from lists.view.index  import do as ListIndex
from lists.view.update import do as ListUpdateView

from stores.view.create import do as StoreCreateView
from stores.view.delete import do as StoreDeleteView
from stores.view.detail import do as StoreDetailView
from stores.view.update import do as StoreUpdateView

from recent.views import RecentDetailView, RecentIndex

from grocerylist.views import LogoutView, LoginView, HelpView, HomeView, MaintenanceView

item_patterns = patterns('',
    #
    # /i/<item pk>/update/
    url(r'^(?P<pk>\d+)/update/$', ItemUpdateView.as_view(), name='update'),
    #
    # /i/<item pk>/delete/
    url(r'^(?P<pk>\d+)/delete/$', ItemDeleteView.as_view(), name='delete'),
)

isle_patterns = patterns('',
    #
    # /s/<store slug>/<isle id>/update/
    url(r'^update/$',  IsleUpdateView.as_view(), name='update'),
    #
    # /s/<store slug>/<isle id>/delete/
    url(r'^delete/$',  IsleDeleteView.as_view(), name='delete'),

)

store_patterns = patterns('',
    #
    # /s/<store slug>/
    url(r'^$',         StoreDetailView.as_view(), name='detail'),
    #
    # devel view of items that belong to this store
    url(r'^inventory/$',   ItemIndex.as_view(), name='inventory'),
    #
    # /s/<store slug>/generate/
    url(r'^generate/$',   ListCreateView.as_view(), name='generate'),
    #
    # /s/<store slug>/update/    
    url(r'^update/$',  StoreUpdateView.as_view(), name='update'),
    #
    # /s/<store slug>/delete/
    url(r'^delete/$',  StoreDeleteView.as_view(), name='delete'),
    #
    # /s/<store slug>/<isle id>/
    url(r'^(?P<pk>[\d]+)/', include(isle_patterns, namespace='isle')),
    #
    # /s/<store slug>/isle-create/
    url(r'^isle/create/$',  IsleCreateView.as_view(), name='isle-create'),
    #
    # /s/<store slug>/item-create/
    url(r'^item/create/$',  ItemCreateView.as_view(), name='item-create'),
    #
    # /s/<store slug>/grocery-lists/
    url(r'^grocery-lists/$',  ListIndex.as_view(), name='grocery-lists'),
)

mylist_patterns = patterns('',
    #
    # /mylists/<item pk>/
    url(r'^(?P<pk>\d+)/$', ListDetailView.as_view(), name='detail'),
    #
    # /mylists/<item pk>/update/
    url(r'^(?P<pk>\d+)/update/', ListUpdateView.as_view(), name='update'),
    #
    # /mylists/<item pk>/delete/
    url(r'^(?P<pk>\d+)/delete/', ListDeleteView.as_view(), name='delete'),
)

recent_patterns = patterns('',
    #
    # /recent/
    url(r'^$', RecentIndex.as_view(), name='index'),
    #
    # /recent/<log pk>/
    url(r'^(?P<pk>\d+)/$', RecentDetailView.as_view(), name='detail'),
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #
    # /
    url(r'^$', HomeView.as_view(), name='index'),
    #
    #
    url(r'^maintenance$', MaintenanceView.as_view(), name='maintenance'),
    #
    #
    url(r'^auth3p$', LoginView.as_view(), name='auth3p'),  # Choose your auth, Twitter/Google/Etc
    url(r'^logout$', LogoutView.as_view(), name='logout'), # Blindly log out any browser that hits this url.
    #
    # Help view
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
