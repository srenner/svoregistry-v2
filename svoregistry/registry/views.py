from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from random import randint
from django.core import serializers
from registry.models import Entry
from registry.models import Car
from json import dumps
from registry.utils import xstr
from registry.forms import AddEntryForm

def coming_soon(request):
    return HttpResponse('Welcome to the future home of the Mustang SVO registry')

def index(request):
    #avoiding order_by('?') because it is a very expensive db call
    entries = Entry.objects.exclude(photo__isnull=True).exclude(photo__exact='').exclude(deleted=True)
    last = entries.count() - 1
    if last >= 0:
        index = randint(0, last)
        random_entry = entries[index]
    else:
        random_entry = None
    return render_to_response('index.html', { 'entry': random_entry }, context_instance=RequestContext(request))

def new(request):
    #display the newest entries
    entries = Entry.objects.order_by('-entry_datetime', '-id').exclude(deleted=True)[:10]
    strJson = serializers.serialize("json", entries)
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

def view_car(request,vin):
    car = Car.objects.get(pk=vin)
    entries = Entry.objects.filter(car=car).exclude(deleted=True).order_by('-entry_datetime')
    if(entries.count() > 0):
        twitter_description = entries[entries.count() - 1].comments[:201]
        if len(twitter_description) == 0:
            twitter_description = 'View info for SVO with VIN ' + car.vin
    else:
        twitter_description = 'View info for SVO with VIN ' + car.vin
    form = AddEntryForm()
    return render_to_response('car.html', {'car': car, 'entries': entries, 'twitter_description': twitter_description, 'form': form}, context_instance=RequestContext(request))

def map_data(request):
    locations = Entry.objects.exclude(geo_lat__isnull=True).exclude(deleted=True)
    json = dumps([{
                   'v': str(l.car),
                   'de': str(xstr(l.year) + ' ' + xstr(l.color)).strip(),
                   'o': xstr(l.owner),
                   'dt': l.entry_datetime.strftime('%b %d, %Y'),
                   'lt': float(l.geo_lat),
                   'lg': float(l.geo_long)
                   } for l in locations])
    return HttpResponse(json, 'application/text')

def map_car(request, vin):
    #car = Car.objects.get(pk=vin)
    entries = Entry.objects.filter(car=vin).exclude(geo_lat__isnull=True).order_by('-entry_datetime').exclude(deleted=True)
    json = dumps([{
                    'entry_id': entry.id,
                    'date': entry.entry_datetime.strftime('%b %d, %Y'),
                    'owner': xstr(entry.owner),
                    'lat': float(entry.geo_lat),
                    'long': float(entry.geo_long)
                  } for entry in entries])
    return HttpResponse(json, 'application/text')

def meta_car(request, vin):
    car = Car.objects.get(pk=vin)
    count = Entry.objects.filter(car=car).exclude(deleted=True).count()
    json = dumps({
                    'year': car.year or 'Unknown',
                    'entry_count': count,
                    'slappers': car.slappers,
                    'color': car.color or 'Unknown',
                    'interior': car.interior or 'Unknown',
                    'sunroof': car.sunroof,
                    'comp_prep': car.comp_prep,
                    'option_delete': car.option_delete,
                    'wing_delete': car.wing_delete,
                    'original_engine': car.has_23,
                    'on_road': car.on_road,
                    'deceased': car.deceased
                })
    return HttpResponse(json, 'application/text')

def flag_entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry.entry_flag += 1
    entry.save()
    return HttpResponse("")