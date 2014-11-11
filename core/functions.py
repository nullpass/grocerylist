# core/functions.py

def navbar(request):
    """
    Return a dict containing all the things
    the html navbar needs to give pretty links
    to all of our apps
        
    Called from settings.py injected into
        TEMPLATE_CONTEXT_PROCESSORS
        
    Using lists because order matters.

    'class_divider' tells the for-loop to
        show a nice hr for that line thereby
        seperating things
    """
    nav_stores = [
        ('Store List',     'index'),
        ('Search',         'index'),
        ('class_divider',  'class_divider'),
        ('Add A Store',    'create'),
        
    ]
    nav_lists = [
        ('My Lists',       'lists:index'),
        ('class_divider',  'class_divider'),
        ('Search',         'index'),
    ]
    navbar = [
        ('Stores',   nav_stores),
        ('My Lists', nav_lists),
    ]
    return { 'navbar' : navbar }
