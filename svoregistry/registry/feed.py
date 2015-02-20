from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from registry.models import Entry

class LatestEntriesFeed(Feed):
    title = "Mustang SVO Registry"
    link = 'http://www.svoregistry.com/new/'
    description = "Newest entries to the SVO Registry"

    def items(self):
        return Entry.objects.order_by('-entry_datetime')[:5]

    def item_title(self, item):
        return item.car_id

    def item_description(self, item):
        return item.comments

    def item_link(self, item):
        return 'http://www.svoregistry.com/' + str(item.car_id) + '/'
        #return reverse('car', args=[item.car_id])