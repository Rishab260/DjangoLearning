from django.shortcuts import render
import django.http


# Create your views here.
def index(request):
    return render(request, "WepApp/index.html ")
