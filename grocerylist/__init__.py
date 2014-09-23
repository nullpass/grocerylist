"""
TODO:

Gotta update all models to include object owner == user
    then update views to assign owner




Continue to contemplate if I'm the only devel who uses the base
    init file as a master todo list.

Audit urls
    maximize urls per page to minimize chance of user getting psudo-lost

lists.
    mark as done href
    
    lists by store (not just related bubble)
    
    change listUpdate.delete_me to redirect to confirm, and confirm = ListDeleteView
    
    all lists should target=_blank
    
    
/recent/
    Not sure if I want to go the whole .logging() route or not, could probably
    just cheat and give recent by object type



/base/urls.py is a monster, keep her that way. kthnx




urlpatterns = patterns('social.apps.django_app.views',
    # authentication / association
    url(r'^login/(?P<backend>[^/]+)/$', 'auth',
        name='begin'),
    url(r'^complete/(?P<backend>[^/]+)/$', 'complete',
        name='complete'),
    # disconnection
    url(r'^disconnect/(?P<backend>[^/]+)/$', 'disconnect',
        name='disconnect'),
    url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>[^/]+)/$',
        'disconnect', name='disconnect_individual'),
)


"""
