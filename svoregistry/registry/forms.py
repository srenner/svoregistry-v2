from django.forms.models import ModelForm
from registry.models import Entry
from django.forms.widgets import Textarea, TextInput

class AddEntryForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('scrape_id', 'ip', 'entry_flag')
        widgets = {
            'car': TextInput(),
            'comments': Textarea(attrs={'rows': 5, 'maxlength': 10000}),
            'mileage': TextInput(attrs={'size': 10 }),
        }
