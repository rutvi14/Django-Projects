from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname)<4:
            raise forms.ValidationError("Value should be more than 4 characters")
        if len(valemail)<10:
            raise forms.ValidationError("Email value should be more than 10 characters")