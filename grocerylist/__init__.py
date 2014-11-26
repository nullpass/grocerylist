"""

TODO:
    (Somewhat sorted by priority)

/*/
    Add maxs to everything


/lists/
    **fix listview, content doesn't exist in form anymore
    lists.models needs new class like the old list_item which can handle quantity
    mark as done href (color coded by status)
    lists by store (not just related bubble)
    all lists should target=_blank
    Add back related gLists somewhere
    List.Done == Convert to text block (flatten) so that future changes to data does not change completed lists.


/isle/    
    Change isle.name from INT to VARCHAR(2) with same regex validator
        a weak hack to support things like "registers" or "stuff on the back wall that isn't itself an isle"
        ya know, isles that don't have numbers, 'cause hippies.
    Add isle.create link back to store.detail.html


/store/
    Gotta do something about slugs. I don't want to force store name and address to be globally unique, but
        manually uniquing slugs is a horror show


/help/
    write dynamic help module that will try to generate help based on whatever is in the url
    Either write a hack to prevent /help/help/help/ or base dynamic help on referal.
    

V5 refactor:
    a. Audit urls. maximize urls per page to minimize chance of user getting psudo-lost
    2. make all object names singular (items>item, stores>store, etc...)
    5. put core.* in ./grocerylist/ 

"""
