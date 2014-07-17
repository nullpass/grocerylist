"""

TODO:

I'm moving linkbox, page/section titles and all that junk to blocks
    keep updating views and templates

Finish removing RenderdataMixin from views that generate dynamic output
    OK to keep for semi-static pages like Create and Update where we
    don't have stuff to draw from already.


Store Detail View has become a fscking monster, trim and refactor her.
    We don't need the next|prev buttons, they are cute but a waste of time.


You forgot to add item.slug (hehe) and that's causing errors further down
    the line with {url} and such.


Either commit to making base.urls a giant beast, or break stores.urls out to
    their related apps.

"""
