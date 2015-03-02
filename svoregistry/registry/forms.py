from django.forms.models import ModelForm
from registry.models import Entry
from django.forms.widgets import Textarea, TextInput, Select, ClearableFileInput, NullBooleanSelect, NumberInput
from django import forms

class AddEntryForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('scrape_id', 'ip', 'entry_flag')
        widgets = {
            'car': TextInput(),
            'year': Select(attrs={ 'class': 'form-control' }),
            'mileage': TextInput(attrs={'size': 10, 'class': 'form-control' }),
            'color': Select(attrs={ 'class': 'form-control' }),
            'interior': Select(attrs={ 'class': 'form-control' }),
            'sunroof': NullBooleanSelect(attrs={ 'class': 'form-control' }),
            #'photo': ClearableFileInput(attrs={ 'class': 'form-control' }),
            
            'owner': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'state': Select(attrs={ 'class': 'form-control' }),
            'country': Select(attrs={ 'class': 'form-control' }),
            'zipcode': TextInput(attrs={'size': 5, 'class': 'form-control' }),
            'entry_datetime': TextInput(attrs={'class': 'form-control'}),
            
            'comp_prep': NullBooleanSelect(attrs={ 'class': 'form-control' }),
            'option_delete': NullBooleanSelect(attrs={ 'class': 'form-control' }),
            'wing_delete': NullBooleanSelect(attrs={ 'class': 'form-control' }),
            'slappers': NullBooleanSelect(attrs={ 'class': 'form-control' }),
            
            'has_23': NullBooleanSelect(attrs={ 'class': 'form-control' }),
            'on_road': NullBooleanSelect(attrs={ 'class': 'form-control' }),
            'deceased': NullBooleanSelect(attrs={ 'class': 'form-control' }),
            
            'list_price': NumberInput(attrs={ 'class': 'form-control' }),
            'transaction_price': NumberInput(attrs={ 'class': 'form-control' }),
                        
            'comments': Textarea(attrs={'rows': 5, 'cols': 120, 'maxlength': 10000, 'placeholder': 'Enter information about the car here.'}),
            'url': TextInput(attrs={'class': 'form-control'})
        }
