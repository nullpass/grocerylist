"""

TODO:
    (Somewhat sorted by priority)


/lists/
    DetailView rewrite done
    Next up, UpdateView (groan)
        Standard edit lets user change quantity.
        Tobuy delete is handled with a [X] url
        Create area on page that lists all items not in list,
            selecting one will make new Tobuy and .add to List.
    Add back related gLists somewhere
    Add (is in my cart) link to each Tobuy item (and add field to model)
        Color code item in List to match (if in-cart then class = foo)
    Add "home form shopping" link that will convert the List object to a multi-
        line string and store it in List.archive.

Tobuy:
    Auto-clean up orphaned tobuy objects.

/isle/    
    Change isle.name from INT to VARCHAR(2) with same regex validator
        a weak hack to support things like "registers" or "stuff on the back wall that isn't itself an isle"
        ya know, isles that don't have numbers, 'cause hippies.
    Add isle.create link back to store.detail.html


/store/
    Gotta do something about slugs. I don't want to force store name and address to be globally unique, but
        manually uniquing slugs is a horror show

/*/
    Add maxs to everything


/help/
    write dynamic help module that will try to generate help based on whatever is in the url
    Either write a hack to prevent /help/help/help/ or base dynamic help on referal.
    

V5 refactor:
    a. Audit urls. maximize urls per page to minimize chance of user getting psudo-lost
    2. make all object names singular (items>item, stores>store, etc...)
    5. put core.* in ./grocerylist/ 

"""
