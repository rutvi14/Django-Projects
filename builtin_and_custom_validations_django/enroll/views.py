from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Registration
# Create your views here.

def showformdata(request):
    if request.method == "POST":
        fm = Registration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            print("Name - {0}, Email - {1}".format(name,email))
            return HttpResponseRedirect("/reg/success")
    else:
        fm = Registration()
    return render(request,"app/registration.html",{"form":fm})

def registration_successful(request):
    return render(request,"app/success.html")
