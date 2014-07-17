# isles/forms.py
from __future__ import absolute_import
#
from django.forms import ModelForm

from . import models

class IsleForm(ModelForm):
    class Meta:
        fields = (
            'name',
            'notes',
            )
        model = models.Isle

    def __init__(self, *args, **kwargs):
        super(IsleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['size'] = 2
        self.fields['notes'].widget.attrs['rows'] = 8
        self.fields['notes'].widget.attrs['cols'] = 16
