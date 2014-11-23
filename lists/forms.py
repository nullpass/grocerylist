# lists/forms.py
from django import forms

from . import models

class ListForm(forms.ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            #'content',
            )
        model = models.List
        widgets = { 'content' : forms.CheckboxSelectMultiple() }

class ListUpdateForm(forms.ModelForm):
    """ """
    deleteme = forms.BooleanField(required=False)
    class Meta:
        fields = (
            'name',
            #'content',
            'done',
            'deleteme',
            )
        model = models.List
        widgets = { 'content' : forms.CheckboxSelectMultiple() }