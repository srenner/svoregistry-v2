from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from random import randint
from django.core import serializers
from registry.models import Entry

def coming_soon(request):
    return HttpResponse('Welcome to the future home of the Mustang SVO registry')

def index(request):
    #avoiding order_by('?') because it is a very expensive db call
    entries = Entry.objects.exclude(photo__isnull=True).exclude(photo__exact='')
    last = entries.count() - 1
    if last >= 0:
        index = randint(0, last)
        random_entry = entries[index]
        strJson = serializers.serialize("json", [random_entry,], excludes=('scrape_id', 'entry_flag', 'ip', 'car'))
    else:
        random_entry = None
        strJson = None
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def new(request):
    #display the newest entries
    entries = Entry.objects.order_by('-entry_datetime', '-id')[:10]
    strJson = serializers.serialize("json", entries, excludes=('scrape_id', 'entry_flag', 'ip', 'comments'))
    return render_to_response("new.html", { 'entries': entries, 'json': strJson }, context_instance=RequestContext(request))

def forsale(request):
    #display SVOs for sale
    template = loader.get_template('forsale.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def statistics(request):
    #display registry statistics
    template = loader.get_template('statistics.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def about(request):
    #display the 'about this site' page
    template = loader.get_template('about.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))