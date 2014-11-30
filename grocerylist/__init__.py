"""

TODO:
    (Somewhat sorted by priority)

***Don't forget to update /static/ if you changed css files. Just cause it's in git doesn't mean it gets updated on `pull`.

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
    

/store/
    Nav tabs are great but it's a ton of repeated code, need to fix that.


/lists/
    Add "home form shopping" link that will convert the List object to a multi-
        line string and store it in List.archive.
    I gutted the messages div on ListDetailView, it was too obnoxious on that view.
        Might need to adjust it again in the future.
    ListUpdateView: Still very unhappy with how the save/cancel/done/delete elements
        look after the V4 refactor. 

/recent/
    V5 broke the name magic in log_form_valid, fit it plox

V6 refactor:
    4. Add delete views for everything.
    s. Rename the directories singular
    1. There is no 'try'; there is only do-and-fail-loudly. Fix that, this is code, not the force.
    2. Update user, add arbitrary dialog flags
    3. Add new user dialogs. X to dismiss, can reset them in user profile.


/filter|search/
    Do the old java style needle-as-argument. Like my inventory app only better.

/maintenance/
    Garbage collection, orphan cleanup.

"""
