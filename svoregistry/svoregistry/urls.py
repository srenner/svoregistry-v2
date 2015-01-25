from django.conf.urls import patterns, include, url
from django.contrib import admin
from registry import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    #uncomment next line to display downtime message on home page
    #url(r'^$', views.coming_soon, name='home'),
    url(r'^$', views.index, name='home'),
    url(r'^new/$', views.new, name='new'),
    url(r'^forsale/$', views.forsale, name='forsale'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^statistics/year/$', views.statistics_year, name='statistics_year'),
    url(r'^statistics/color/$', views.statistics_color, name='statistics_color'),
    url(r'^statistics/status/$', views.statistics_status, name='statistics_status'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<vin>\w{17})/$', views.view_car, name='car'),
    url(r'^map/(?P<vin>\w{17})/$', views.map_car, name='map_car'),
    url(r'^meta/(?P<vin>\w{17})/$', views.meta_car, name='meta_car'),
    url(r'^lookup$', views.lookup_car, name='lookup'),
    url(r'^map/', views.map_data, name='map_data'),
    url(r'^flag/(?P<entry_id>\d+)/$', views.flag_entry, name='flag_entry'),
    url(r'^download/$', views.download, name='download'),
    url(r'^validate/(?P<vin>\w+)/$', views.validate, name='validate'),


    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
