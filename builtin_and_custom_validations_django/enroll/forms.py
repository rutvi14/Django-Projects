from wsgiref.validate import validator
from django import forms
from django.core import validators


def start_with_special_characters(value):
    if value.isalnum:
        raise forms.ValidationError("Name should not contain numbers.")


class Registration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])  # built-in
    name = forms.CharField(validators=[start_with_special_characters])  # custom validation
    email = forms.EmailField()
