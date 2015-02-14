# items/forms.py

from django.forms import ModelForm, CheckboxSelectMultiple, RadioSelect

from . import models


class EmbedItemForm(ModelForm):
    """ The item-add form that is embedded in StoreDetailView.html """
    
    class Meta:
        fields = (
            'name',
            'price',
            'from_isle',
            )
        model = models.Item

    def __init__(self, *args, **kwargs):
        super(EmbedItemForm, self).__init__(*args, **kwargs)
        self.fields['from_isle'].empty_label = None
        self.fields['name'].widget.attrs['size'] = 20
        self.fields['from_isle'].widget.attrs['style'] = 'width: 150px;'


class ItemForm(ModelForm):
    """ A standard item create form """
    
    class Meta:
        fields = (
            'name',
            'price',
            'from_isle',
            )
        model = models.Item
        widgets = {'from_isle': RadioSelect() }

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['from_isle'].empty_label = None
