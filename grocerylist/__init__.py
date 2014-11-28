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
    ListDetailView - That 'edit' button is at the bottom of the page,
        we need to keep discussing that, there has to be a better
        place for it. 
    Add back related gLists somewhere
    Add "home form shopping" link that will convert the List object to a multi-
        line string and store it in List.archive.
    I gutted the messages div on ListDetailView, it was too obnoxious on that view.
        Might need to adjust it again in the future.
    ListUpdateView: Still very unhappy with how the save/cancel/done/delete elements
        look after the V4 refactor. 

Tobuy:
    Auto-clean up orphaned tobuy objects.

/isle/    
    Change isle.name from INT to VARCHAR(2) with same regex validator
        a weak hack to support things like "registers" or "stuff on the back wall that isn't itself an isle"
        ya know, isles that don't have numbers, 'cause hippies.
    Add isle.create link back to store.detail.html



/*/
    Add maxs to everything

/-/
    [AFTER V5], start making delete views for everything.

/help/
    write dynamic help module that will try to generate help based on whatever is in the url
    Either write a hack to prevent /help/help/help/ or base dynamic help on referal.
    

V5 refactor:
    _. Start moving every view to its own file. Yes we are at that point; past it, actually.
    a. Audit urls. maximize urls per page to minimize chance of user getting psudo-lost
    2. make all object names singular (items>item, stores>store, etc...)
    5. put core.* in ./grocerylist/ 

"""
