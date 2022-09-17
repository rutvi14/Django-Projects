from django import forms


class Registration(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput, label="Enter your password again ")

    def clean(self):
        cleaned_data = super().clean()
        passwd = cleaned_data.get("password")
        rpasswd = cleaned_data.get("rpassword")
        if passwd != rpasswd:
            raise forms.ValidationError("Both passwords must be same. Please enter your password again !!")
