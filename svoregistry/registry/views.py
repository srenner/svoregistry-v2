from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from random import randint
from django.core import serializers
from registry.models import Entry
from registry.models import Car
from json import dumps
from registry import geocoder
from registry.utils import xstr
from registry.utils import validate_vin
from registry.utils import dictfetchall
from registry.forms import AddEntryForm
from django.http.response import HttpResponseRedirect
from django.db import connection
import json
import csv
from django.shortcuts import redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings

def coming_soon(request):
    return HttpResponse('Welcome to the future home of the Mustang SVO registry')

@ensure_csrf_cookie
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

def lookup_car(request):
    vin = request.GET.get('vin').upper() #capture vin in query string for noscript form compatibility
    try:
        car = Car.objects.get(pk=vin)
        if request.is_ajax():
            return HttpResponse("1") #car was found
        else:
            return redirect('car', vin=vin) #car was found
    except Car.DoesNotExist:
        if request.is_ajax():
            return HttpResponse("0") #car not found
        else:
            if validate_vin(vin)['valid']:
                return render_to_response('lookup_add.html', { 'vin': vin }, context_instance=RequestContext(request)) #car not found
            else:
                return render_to_response('lookup_invalid.html', { 'vin': vin }, context_instance=RequestContext(request)) #vin was invalid

def new(request):
    #display the newest entries
    entries = Entry.objects.order_by('-entry_datetime', '-id').exclude(deleted=True)[:5]
    strJson = serializers.serialize("json", entries)
    return render_to_response("new.html", { 'entries': entries, 'json': strJson }, context_instance=RequestContext(request))

def forsale(request):
    #display SVOs for sale
    entries = Entry.objects.filter(for_sale=True).order_by('-entry_datetime').exclude(deleted=True)[:5]
    strJson = serializers.serialize("json", entries)
    return render_to_response("forsale.html", { 'entries': entries, 'json': strJson }, context_instance=RequestContext(request))

def statistics(request):
    #display registry statistics
    cursor = connection.cursor()
    cursor.execute("select count(*) from registry_car")
    cars = cursor.fetchall()[0][0]
    
    cursor = connection.cursor()
    cursor.execute("select count(*) from registry_entry")
    entries = cursor.fetchall()[0][0]    
    
    return render_to_response("statistics.html", {'cars': cars, 'entries': entries}, context_instance=RequestContext(request))

def statistics_year(request):
    cursor = connection.cursor()
    cursor.execute("""select year, count(year) as "count",
                          case year
                            when '1984' then 4506
                            when '1985' then 1512
                            when '1985.5' then 439
                            when '1986' then 3378
                          end as "total_production"
                        from registry_car
                        where year != 'NULL'
                        group by year order by year""")
    report = dictfetchall(cursor)
    return HttpResponse(json.dumps(report), 'application/json')

def statistics_color(request):
    cursor = connection.cursor()
    cursor.execute("""select color, count(color) as "count"
                        from registry_car
                        where color != 'NULL'
                        group by color order by color""")
    report = dictfetchall(cursor)
    return HttpResponse(json.dumps(report), 'application/json')

def statistics_status(request):
    cursor = connection.cursor()
    cursor.execute("""select
                          case deceased
                            when True then 'Deceased'
                            when False then 'Alive'
                          end as "status",
                          count(deceased) as "count"
                        from registry_car
                        where deceased is not null
                        group by deceased
                        union all
                        select 
                          'Unknown' as "status", 
                          (select count(*) from registry_car where deceased is null) as "count"
                          """)
    report = dictfetchall(cursor)
    return HttpResponse(json.dumps(report), 'application/json')

def statistics_entry_year(request):
    cursor = connection.cursor()
    cursor.execute("""select count(id) as count, extract(year from date(entry_datetime)) as entry_year
                        from registry_entry
                        group by entry_year
                        order by entry_year""")
    report = dictfetchall(cursor)
    return HttpResponse(json.dumps(report), 'application/json')

def about(request):
    #display the 'about this site' page
    template = loader.get_template('about.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def download(request):
    excludes = ['scrape_id', 'entry_flag', 'ip', 'deleted']
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=svo_export.csv'
    writer = csv.writer(response)
    headers = []
    for field in Entry._meta.fields:
        do_write = True
        pass
        for exclude in excludes:
            if exclude == field.name:
                do_write = False
                break
        if do_write:
            headers.append(field.name)
    writer.writerow(headers)
    for obj in Entry.objects.exclude(deleted=True).order_by("id"):
        row = []
        for field in Entry._meta.fields:
            do_write = True
            for exclude in excludes:
                if exclude == field.name:
                    do_write = False
                    break
            if do_write:
                row_content = getattr(obj, field.name)
                row.append(row_content)
        writer.writerow(row)
    return response

def geocode(request):
    return HttpResponse(geocoder.geocode(settings.DB_PASS))

@ensure_csrf_cookie
def add_car(request, vin):
    vin = vin.upper()
    carObject = Car(vin=vin, year = validate_vin(vin)['year'])
    carObject.save()
    return HttpResponseRedirect('/' + vin + '/')

def refresh_car(request, vin):
    car = Car.objects.get(pk=vin)
    metadata = loader.render_to_string("car_metadata.html", {'car': car})
    header =  loader.render_to_string("car_header.html", {'car': car})
    json = dumps({
                   'metadata': metadata,
                   'header': header
                   })
    return HttpResponse(json, 'application/json')

def add_entry(request):
    vin=''
    user_ip = request.META['HTTP_X_REAL_IP']
    if request.method == 'POST':
        form = AddEntryForm(request.POST)
        if form.is_valid():
            vin=str(form.cleaned_data['car'])
            carObject = Car(vin=vin, year=form.cleaned_data['year'], slappers=form.cleaned_data['slappers'], color=form.cleaned_data['color'], 
                      interior=form.cleaned_data['interior'], sunroof=form.cleaned_data['sunroof'], comp_prep=form.cleaned_data['comp_prep'], 
                      option_delete=form.cleaned_data['option_delete'], wing_delete=form.cleaned_data['wing_delete'], 
                      has_23=form.cleaned_data['has_23'], on_road=form.cleaned_data['on_road'], deceased=form.cleaned_data['deceased'])
            carObject.save()
            #TODO: reduce db calls
            new_entry = form.save()
            new_entry.ip = user_ip
            new_entry.save()
            if request.FILES.get("photo"):
                new_entry.photo = request.FILES['photo']
                new_entry.save()
            if request.is_ajax():
                return render_to_response("entry.html", { 'entry': new_entry }, context_instance=RequestContext(request))

    return HttpResponseRedirect('/' + vin)

@ensure_csrf_cookie
def view_car(request,vin):
    car = Car.objects.get(pk=vin)
    entries = Entry.objects.filter(car=car).exclude(deleted=True).order_by('-entry_datetime', '-id')
    if(entries.count() > 0):
        twitter_description = entries[entries.count() - 1].comments[:201]
        if len(twitter_description) == 0:
            twitter_description = 'View info for SVO with VIN ' + car.vin
    else:
        twitter_description = 'View info for SVO with VIN ' + car.vin
    form = AddEntryForm({'car': vin})
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
    return HttpResponse(json, 'application/json')

def car_entries(request, vin):
    entries = Entry.objects.filter(car=vin).order_by('entry_datetime').exclude(deleted=True)
    json = dumps([{
                    'entry_id': entry.id,
                    'date': entry.entry_datetime.strftime('%b %d, %Y'),
                    'dateformat': entry.entry_datetime.strftime('%Y-%m-%d'),
                    'owner': xstr(entry.owner),
                    'location': (xstr(entry.city) + ' ' + xstr(entry.state) + ' ' + xstr(entry.country)).strip(),
                    'lat': float('0' if entry.geo_lat is None else str(entry.geo_lat)),
                    'long': float('0' if entry.geo_long is None else str(entry.geo_long))
                  } for entry in entries])
    return HttpResponse(json, 'application/json')       

def flag_entry(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
        entry.entry_flag += 1
        entry.save()
    except Entry.DoesNotExist:
        pass
    return HttpResponse("")

def validate(request, vin):
    vin = vin.upper()
    return HttpResponse(json.dumps(validate_vin(vin)), content_type="application/json")
