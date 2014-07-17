"""

TODO:

I'm moving linkbox, page/section titles and all that junk to blocks
    keep updating views and templates

Finish removing RenderdataMixin from views that generate dynamic output
    OK to keep for semi-static pages like Create and Update where we
    don't have stuff to draw from already.

Store Detail View has become a fscking monster, trim and refactor her.

Either commit to making base.urls a giant beast, or break stores.urls out to
    their related apps.


@migration required
lists.status (new|done)
    if 'done' then `strike-through` in storedetail.related_lists and lists.index
    add listUpdateview
    


"""
