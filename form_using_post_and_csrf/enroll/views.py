from django.shortcuts import render
from .forms import Registration
# Create your views here.

def showformdata(request):
    if request.method == "POST":
        fm = Registration(request.POST)
        if fm.is_valid():
            print("Form validated")
            # name= request.POST['name'] you can also access this way or from cleaned_data dict
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            print("Name - {0}, Email - {1}, password - {2}".format(name,email,password))
            fm = Registration()
    else:
        fm = Registration()
    return render(request,"app/registration.html",{"form":fm})

#you can use novalidate attribute in form tag to disable html validation and see django validation 
#if form is not valid it will show error on UI and will go into else part here.