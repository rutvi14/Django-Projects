from django.shortcuts import render
from .forms import Registration
# Create your views here.

def showformdata(request):
    fm = Registration()
    return render(request,"app/registration.html",{"form":fm})