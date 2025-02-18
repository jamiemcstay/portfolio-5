from django import forms
from .models import NewsLetterSubscription
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterSubscription
        fields = ['email']

    def __init__(self, *args, **kwargs):
        # Prevent pre population of data (remove user data)
        kwargs.pop('instance', None)
        # Call parent class __init__ method to ensure form works as expected
        super(NewsLetterForm, self).__init__(*args, **kwargs)
        # Initialize FormHelper from CrispyForms to customize form layout
        self.helper = FormHelper()

        self.helper.form_class = 'form-inline justify-content-center'

        self.helper.add_input(Submit('submit', 'Subscribe'))
