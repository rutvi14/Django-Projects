from django import forms

class Registration(forms.Form):
    name = forms.CharField(label="Full Name",label_suffix=" ",initial="Rutvi ",help_text="FirstName Surname FaterName")
    #required = False for optional field
    #disabled = True for disabling field

    