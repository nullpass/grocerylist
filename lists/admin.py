# tickets/admin.py
from django.contrib import admin

from lists.models import List, Tobuy
admin.site.register(List)
admin.site.register(Tobuy)

