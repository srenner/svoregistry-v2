from django.contrib.sitemaps import Sitemap
from registry.models import Car
from django.core.urlresolvers import reverse

class CarSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Car.objects.all()

class StaticViewSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return ['home', 'new', 'statistics', 'about']

    def location(self, item):
        return reverse(item)



    #def lastmod(self, obj):
    #    return obj.pub_date