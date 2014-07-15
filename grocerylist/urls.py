from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from stores import views

from lists.views import ListDetailView

list_pats = patterns('',
    #
    url(r'^(?P<pk>\d+)/$', ListDetailView.as_view(), name='detail')
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #
    url(r'^$', views.Index.as_view(), name='index'),
    #
    url(r'^s/(?P<slug>[\w-]+)/', include('stores.urls',   namespace='stores')),
    #
    url(r'^create/', views.StoreCreateView.as_view(), name='create'),
    #
    url(r'^lists/', include(list_pats, namespace='lists')),
    #
    # url(r'^recent/', views.RecentView.as_view(), name='recent'),
)
