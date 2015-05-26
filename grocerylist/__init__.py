"""

TODO:
    (Somewhat sorted by priority)

Put done lists in their own view, make only open lists visible on main pages.


***If /static/ changes remember to copy them over to the static server in prod.

**I would really like it if the next refactor didn't require a db migration. Baby Jesus is already so very sad. 

*Code cleanse:
    from django.shortcuts import get_object_or_404
    context['store'] = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        and
    context['back'] = self.object.store.get_absolute_url()
        or
    context['back'] = context['store'].get_absolute_url()

    When making a QuerySet, always make the first .filter() user.
    ALWAYS filter by user, especially when it's silly.
    Prefer get|404 to a simple get().
    If something is ugly but I don't have a fix, ignore it. 

/recent/
    action is fixed, but it looks like we don't need the form argument and I can merge
        both functions. I wonder if form is an artifact from ksdj; the current ksdj
        doesn't use form either. 


/filter|search/
    Do the old java style needle-as-argument. Like my inventory app only better.

"""
    