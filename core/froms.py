from django import forms
from django_countries.fields import CountryField


PAYMENT_CHOICES = (
    ('J', 'JCB'),
    ('V', 'Visa'),
    ('M', 'MasterCard'),
)


class CheckourForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' 1234 Main St',
        'class': 'form-control'
    }))
    apartemnt_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': ' Apartment or suite',
        'class': 'form-control'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' Abcd',
        'class': 'form-control'
    }))
    '''country = CountryField(blank_label='(select country)').formfield(attrs={
        'class': 'custom-select d-block w-100'
    })
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())'''
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
