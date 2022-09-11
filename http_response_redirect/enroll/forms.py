from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':"Enter your password"})
    #using error_messages you can override different error messages.