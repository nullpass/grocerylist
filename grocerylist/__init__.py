"""

TODO:

2. There are ownership landmines, clean them up
    +All of the ownership landminds in views seem to be fixed. All '.objects.' calls include ownership filters
    and all create views already assigned owners on form_valid.
3. Remove use of name 'item' or 'items', replace with 'content' or 'inventory'.
4. Refactor Items and Isles into Store
5. Make everything singular 
6. List.Done == Convert to text block (flatten) so that future changes to data does not change completed lists.
7. Not entirely sure what my plans were with the human app. Sign-in will always only be with 'social'


Audit urls
    maximize urls per page to minimize chance of user getting psudo-lost

lists.
    mark as done href (color coded by status)
    lists by store (not just related bubble)
    all lists should target=_blank
    Delete == remove from visibility
    
/recent/
    Not sure if I want to go the whole .logging() route or not, could probably
    just cheat and give recent by object type

/base/urls.py is a monster, keep her that way. kthnx

"""
