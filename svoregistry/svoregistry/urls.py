from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #uncomment next line to display downtime message on home page
    #url(r'^$', 'registry.views.coming_soon', name='home'),
    url(r'^$', 'registry.views.index', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    
)
