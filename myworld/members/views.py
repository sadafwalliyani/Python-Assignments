# from django.shortcuts import render
# # Create your views here.
# from django.template import loader
# from django.http import HttpResponse

# def index(request):
#     template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())
    
#     # return HttpResponse("Hello world!")

# template = loader.get_template('myfirst.html')
# return HttpResponse(template.render())
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context,request))
  # output = ""
  # for x in mymembers:
  #   output += x["firstname"]
  # return HttpResponse(output)

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({},request))

def addrecord(request):
 x = request.POST['first']
 y = request.POST['last']
 member=Members(firstname=x, lastname=y)
 member.save()
 return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member=Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))