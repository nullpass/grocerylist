"""

TODO:

/recent/


The V4 refactor will redo how we apporach Item objects. I am delaying the start until
    I will have time to get a working rev out. For now I'm just letting the ideas cook.
    
    
V4:
    Remove FKeys from Item.models.
    Isle.models now have M2M attr 'content' that links Item.models
    List.content now points to Isle.models (instead of Item.models)
        All of this allows us to easily present items grouped by isle which was the whole point all along.
    Moving to newRoot.html which does away with info boxes in favor of a wider default view.
    Links that used to be in info boxes get moved to the header menu.
    Header menu will need to be refactored for dynamic updates.

V5:
    In code (not template)
        Rename Item[s] to Food
        Rename Isle[s] to Lane



The last-change|created boxes on store.detailview are not clearly refering to the store.
    Consider moving them to store.updateview, mouseover text or someplace generally less visible.
    Or merge store.address, store.notes with born&changed into one info box.

Add 'Edit this store' link on right during store.detailview, it's redundant but user-friendly.
    ---CANCEL, just move all menu items to the header, we're getting rid of info boxes

New isles are invisible until an item is added to them. Not sure how to fix that but it needs fixing.

Change isle.name from INT to VARCHAR(2) with same regex validator

Change the item-isle relationship from item.fk>isle to isle.m2m>items
    then write a special "move item to different isle" method in item.updateview
    Later, find some collapse css for isles

Idealy store.detailview should show isles in boxes  that scroll right on regular monitors and scroll
    down on mobile (Sorted numerically by isle number, obviously) and now just a flat list that gets
    out of control with lists of any realistic size.
    This probably means getting rid of the info boxes, putting all links in the top menu and spreading
    the store info box out to be a wide header, then putting all of the user-touchable stuff below (hehe)
    
Add isle.create link back to store.detail.html


List.Done == Convert to text block (flatten) so that future changes to data does not change completed lists.

Audit urls. maximize urls per page to minimize chance of user getting psudo-lost

lists.
    mark as done href (color coded by status)
    lists by store (not just related bubble)
    all lists should target=_blank
    

/base/urls.py is a monster, keep her that way. kthnx
    Dear past me, WHY!?!?!?!?!?!?!?!!?!?!?!!?!?!?!?!?!??!1/1//1//1/


In your next life when you do a full refactor of this program do this:
    1. rename items to food (ignore that not all things are food, just makes code easier to read)
    2. make all object names singular (items>item, stores>store, etc...)
    3. make isle a submod of store
    4. make foor a submod of isle
    5. put core.* in ./grocerylist/ (basically trying to reduce the number of dirs at root)
"""
