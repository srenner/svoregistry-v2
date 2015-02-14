import datetime
from haystack import indexes
from registry.models import Entry

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    creation_date = indexes.DateTimeField(model_attr='entry_datetime')

    def get_model(self):
        return Entry

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects#.filter(deleted == False)