from django import forms


class ContactForm (forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Your Email Address'}))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 4, 'placeholder':
                            'Your Message'}), required=True)
