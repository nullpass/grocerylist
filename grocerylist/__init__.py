"""

TODO:

2. There are ownership landmines, clean them up
    foo = This.objects.filter(user=self.request.user).etc
3. Remove use of name 'item' or 'items', replace with 'content' or 'inventory'.
4. Refactor Items and Isles into Store
5. Make everything singular 
6. List.Done == Convert to text block (flatten) so that future changes to data does not change completed lists.

Audit urls
    maximize urls per page to minimize chance of user getting psudo-lost

lists.
    mark as done href (color coded by status)
    lists by store (not just related bubble)
    all lists should target=_blank
    Delete == remove from visibility

An empty isle gets smushed upwards, need to inject a break
    If isle 1 is empty, but isle 2 has items then isle 2 gets pushed up into isle 1
    
/recent/
    Not sure if I want to go the whole .logging() route or not, could probably
    just cheat and give recent by object type

/base/urls.py is a monster, keep her that way. kthnx

"""
