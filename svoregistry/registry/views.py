from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def coming_soon(request):
    return HttpResponse('Welcome to the future home of the Mustang SVO registry')

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))