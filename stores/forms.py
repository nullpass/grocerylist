# stores/forms.py

from django.forms import ModelForm, Form, CheckboxSelectMultiple
from django.db.models import BooleanField, ManyToManyField

from items.models import Item

from . import models


class StoreForm(ModelForm):
    class Meta:
        fields = (
            'name',
            'address',
            'notes',
            )
        model = models.Store
    
    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['size'] = 64
        self.fields['address'].widget.attrs['size'] = 64
        self.fields['notes'].widget.attrs['rows'] = 2
        self.fields['notes'].widget.attrs['cols'] = 64
