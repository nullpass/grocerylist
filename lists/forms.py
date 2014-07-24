# lists/forms.py

from __future__ import absolute_import

#from django.forms import ModelForm, CheckboxSelectMultiple
from django import forms

from . import models

class ListForm(forms.ModelForm):
    class Meta:
        fields = (
            'name',
            'items',
            )
        model = models.List
        widgets = { 'items' : forms.CheckboxSelectMultiple() }



class ListUpdateForm(forms.ModelForm):
    delete_me = forms.BooleanField(required=False)
    class Meta:
        fields = (
            'name',
            'items',
            'done',
            'delete_me',
            )
        model = models.List
        widgets = { 'items' : forms.CheckboxSelectMultiple() }
