from django.shortcuts import render, HttpResponse
from django import *
from datetime import date, timedelta
from RegApp.models import StudentModel

def register(request):
    todaysdate = date.today()
    todaysdate += timedelta(days=10)
    return render(request, 'RegApp/register.html', {'lastdate': todaysdate})


def save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = StudentModel(name=name,subject=subject,email=email,message=message)
        data.save()
    return HttpResponse(f"<h1 style= 'align='center';> Thank You! </h1> <h2>We will get back to you soon , {name} </h2>")

def display(request):
    data = StudentModel.objects.all()
    datadict = {'data':data}
    return render(request,"details.html",datadict)
