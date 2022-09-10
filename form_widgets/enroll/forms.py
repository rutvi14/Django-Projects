from django import forms

class Registration(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(widget=forms.Textarea)
    Resume = forms.CharField(widget=forms.FileInput)
    Receive_Mail = forms.CharField(widget=forms.CheckboxInput)
    #HiddenInput - for hidden field
    #Textarea
    #TextInput(attrs = {"class":"classname","id": "idname"}) for setting attributes of widget we can give dictionary like this.