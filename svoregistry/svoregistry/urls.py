from django.conf.urls import patterns, include, url
from django.contrib import admin
from registry import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    #url(r'^$', views.coming_soon, name='home'),
    url(r'^$', views.index, name='home'),                                                       #landing page
    url(r'^new/$', views.new, name='new'),                                                      #simple page
    #url(r'^forsale/$', views.forsale, name='forsale'),                                         #may not use
    url(r'^about/$', views.about, name='about'),                                                #simple page
    
    url(r'^map/', views.map_data, name='map_data'),                                             #json
    
    url(r'^geocode/$', views.geocode, name='geocode'),                                          #execute geocode script, do nothing
    
    url(r'^download/$', views.download, name='download'),                                       #csv output
    
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^statistics/year/$', views.statistics_year, name='statistics_year'),                  #json
    url(r'^statistics/timeline/$', views.statistics_entry_year, name='statistics_entry_year'),  #json
    url(r'^statistics/color/$', views.statistics_color, name='statistics_color'),               #json
    url(r'^statistics/status/$', views.statistics_status, name='statistics_status'),            #json
    
    
    url(r'^(?P<vin>\w{17})/$', views.view_car, name='car'),                                     #main car page
    #url(r'^map/(?P<vin>\w{17})/$', views.map_car, name='map_car'),                              #get map for car
    url(r'^entries/(?P<vin>\w{17})/$', views.car_entries, name='car_entries'),                  #get json entries for car
    url(r'^flag/(?P<entry_id>\d+)/$', views.flag_entry, name='flag_entry'),                     #ajax post

    url(r'^lookup$', views.lookup_car, name='lookup'),                                          #adding vin
    url(r'^validate/(?P<vin>\w+)/$', views.validate, name='validate'),                          #adding vin
    
    url(r'^add$', views.add_entry, name='add_entry'),                                           #add entry
    url(r'^add/(?P<vin>\w+)/$', views.add_car, name='add_car'),                                 #add car without entry
    url(r'^refresh/(?P<vin>\w+)/$', views.refresh_car, name='refresh_car'),                     #called after adding an entry

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
