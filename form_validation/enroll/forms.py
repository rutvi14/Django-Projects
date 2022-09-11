from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':"Enter your password"})
    #using error_messages you can override different error messages.
    # def clean_password(self):
    #     pd = self.cleaned_data.get("password")
    #     name = self.cleaned_data['name']
    #     if len(pd)<8:
    #         raise forms.ValidationError("Password length must be atleast 8 characters.")
    # For cleaning one field you can use this function otherwise below one.

    def clean(self):
        cleaned_data = super().clean()
        pd = self.cleaned_data["password"]
        name = self.cleaned_data['name']
        if len(pd)<8:
            raise forms.ValidationError("Password length must be atleast 8 characters.")
        if len(name)<2:
            raise forms.ValidationError("Name length should more than 2 characters.")
        