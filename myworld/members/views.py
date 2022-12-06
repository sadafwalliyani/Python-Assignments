# from django.shortcuts import render
# # Create your views here.
# from django.template import loader
# from django.http import HttpResponse

# def index(request):
#     template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())
    
#     # return HttpResponse("Hello world!")

from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())