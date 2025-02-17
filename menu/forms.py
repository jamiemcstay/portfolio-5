from django import forms
from .models import MenuItem, Category


class MenuItemForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'image_url', 'category']
