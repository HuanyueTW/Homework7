#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myIndex(request):
    my_name=request.GET.get('name',"Huanyue")
    return HttpResponse("Hello " + my_name + ". This is homework7 by B0644247")