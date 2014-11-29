"""

TODO:
    (Somewhat sorted by priority)

***Don't forget to update /static/ if you changed css files. Just cause it's in git doesn't mean it gets updated on `pull`.

**I would really like it if the next refactor didn't require a db migration. Baby Jesus is already so very sad. 


/store/
    |Edit|Add-Isle|Add-Item|List-Lists| can all be tabs on the top of the Store-Info box, just
        gotta remember where I saw that css. WTB a WebDev.
    Gotta do something about slugs. I don't want to force store name and address to be globally unique, but
        manually uniquing slugs is a horror show


/lists/
    related-grocery-lists: Add back when you impliment tabs, and use bages to show how
        many lists there are for that store.
    Add "home form shopping" link that will convert the List object to a multi-
        line string and store it in List.archive.
    I gutted the messages div on ListDetailView, it was too obnoxious on that view.
        Might need to adjust it again in the future.
    ListUpdateView: Still very unhappy with how the save/cancel/done/delete elements
        look after the V4 refactor. 


.____________.__________.___________________.__________.
| edit store | add isle | grocery lists (2) | foo-bar  |
|            |          |                   |          |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Store name
  store address.address.address zip code etc
  notes about store notes notes notes
  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


/help/
    write dynamic help module that will try to generate help based on whatever is in the url
    Either write a hack to prevent /help/help/help/ or base dynamic help on referal.
    

V5 refactor:
    _. Start moving every view to its own file. Yes we are at that point; past it, actually.
    a. Audit urls. maximize urls per page to minimize chance of user getting psudo-lost


V6 refactor:
    1. There is no 'try'; there is only do-and-fail-loudly. Fix that, this is code, not the force.
    2. Update user, add arbitrary dialog flags
    3. Add new user dialogs. X to dismiss, can reset them in user profile.
    4. Add delete views for everything.

"""
