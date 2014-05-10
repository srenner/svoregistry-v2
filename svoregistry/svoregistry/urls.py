from django.conf.urls import patterns, include, url
from django.contrib import admin
from registry import views

urlpatterns = patterns('',
    #uncomment next line to display downtime message on home page
    #url(r'^$', views.coming_soon, name='home'),
    url(r'^$', views.index, name='home'),
    url(r'^new/$', views.new, name='new'),
    url(r'^forsale/$', views.forsale, name='forsale'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^about/$', views.about, name='about'),
    url(r'^admin/', include(admin.site.urls)),
    
)
