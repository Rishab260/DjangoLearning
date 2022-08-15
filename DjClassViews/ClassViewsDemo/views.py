from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import View, TemplateView


# Create your views here.
class CBV(View):
    def get(self, request):
        return HttpResponse("<h1 style='color:red'>Welcome to Class Based Views</h1>")

    def post(self, request):
        return HttpResponse("Thank U")


