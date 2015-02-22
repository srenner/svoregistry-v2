from django.db import models
from localflavor.us.us_states import US_STATES
from localflavor.ca.ca_provinces import PROVINCE_CHOICES

class Car(models.Model):
    COLOR_CHOICES = (
        ('1B','1B (Medium Charcoal)'),
        ('1C','1C (Black)'),
        ('1D', '1D (Dark Gray)'),
        ('1E', '1E (Silver)'),
        ('2A', '2A (Medium Canyon Red)'),
        ('2R', '2R (Jalepeno Red)'),
        ('4E', '4E (Dark Sage)'),
        ('7B', '7B (Dark Shadow Blue)'),
        ('9L', '9L (Oxford White)'),
        ('9W', '9W (Dark Charcoal)'),
        (''  , 'Unknown or Custom')
    )
    vin = models.CharField(max_length=17, primary_key=True, unique=True)
    #these fields are in two models in case users disagree about what the car has
    #the Car model will hold the most recent information about the car
    year = models.CharField(max_length=6, null=True, blank=True)
    slappers = models.NullBooleanField(default=False, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    interior = models.CharField(max_length=50, null=True, blank=True)
    sunroof = models.NullBooleanField(default=False, null=True, blank=True)
    comp_prep = models.NullBooleanField(default=False, null=True, blank=True)
    option_delete = models.NullBooleanField(default=False, null=True, blank=True)
    wing_delete = models.NullBooleanField('Bi-Wing delete', default=False, null=True, blank=True)
    has_23 = models.NullBooleanField('Has 2.3L', default=True, null=True, blank=True)
    on_road = models.NullBooleanField(default=True, null=True, blank=True)
    deceased = models.NullBooleanField(default=False, null=True, blank=True)
    #
    def get_absolute_url(self):
        return "/" + self.vin + "/"
    def __str__(self):
        return self.vin
    
def content_file_name(instance, filename):
    return '/'.join(['content', instance.pk, filename])
    
class Entry(models.Model):
    YEAR_CHOICES = (
        ('1984', '1984'),
        ('1985', '1985'),
        ('1985.5', '1985.5'),
        ('1986', '1986'),
    )
    STATE_CHOICES = US_STATES + PROVINCE_CHOICES
    COUNTRY_CHOICES = (
        ('USA', 'USA'),
        ('CA', 'Canada'),
        ('', 'Other Country')
    )
    COLOR_CHOICES = (
        ('1B','1B (Medium Charcoal)'),
        ('1C','1C (Black)'),
        ('1D', '1D (Dark Gray)'),
        ('1E', '1E (Silver)'),
        ('2A', '2A (Medium Canyon Red)'),
        ('2R', '2R (Jalepeno Red)'),
        ('4E', '4E (Dark Sage)'),
        ('7B', '7B (Dark Shadow Blue)'),
        ('9L', '9L (Oxford White)'),
        ('9W', '9W (Dark Charcoal)'),
        (''  , 'Unknown or Custom')
    )
    INTERIOR_CHOICES = (
        ('Cloth', 'Cloth'),
        ('Leather', 'Leather')
    )
    
    car = models.ForeignKey(Car)
    scrape_id = models.IntegerField(null=True, blank=True)
    #these fields are in two models in case users disagree about what the car has
    #the Car model will hold the most recent information about the car
    year = models.CharField(max_length=6, choices=YEAR_CHOICES, null=True, blank=True)
    slappers = models.NullBooleanField(default=False, null=True, blank=True)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, null=True, blank=True)
    interior = models.CharField(max_length=50, choices=INTERIOR_CHOICES, null=True, blank=True)
    sunroof = models.NullBooleanField(default=False, null=True, blank=True)
    comp_prep = models.NullBooleanField(default=False, null=True, blank=True)
    option_delete = models.NullBooleanField(default=False, null=True, blank=True)
    wing_delete = models.NullBooleanField('Bi-Wing delete', default=False, null=True, blank=True)
    has_23 = models.NullBooleanField('Has 2.3L', default=True, null=True, blank=True)
    on_road = models.NullBooleanField(default=True, null=True, blank=True)
    deceased = models.NullBooleanField(default=False, null=True, blank=True)
    #
    for_sale = models.BooleanField(default=False)
    entry_datetime = models.DateTimeField(auto_now=False, verbose_name='Entry Date')
    owner = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True, choices=STATE_CHOICES)
    country = models.CharField(max_length=255, null=True, blank=True, choices=COUNTRY_CHOICES, default="USA")
    zipcode = models.CharField(max_length=15, null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=10000, null=True, blank=True)
    entry_flag = models.IntegerField(default=0, null=True, blank=True)
    #photo = StdImageField(upload_to='photos', null=True, blank=True, size=(1000, 750))
    photo_height = models.PositiveIntegerField(null=True, blank=True)
    photo_width = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos', null=True, blank=True, height_field='photo_height', width_field='photo_width')
    ip = models.CharField(max_length=50, default='?', null=True, blank=True)
    geo_lat = models.DecimalField(decimal_places=8, max_digits=11, null=True, blank=True)
    geo_long = models.DecimalField(decimal_places=8, max_digits=11, null=True, blank=True)
    actual_entry_datetime = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'Entries'
    def get_absolute_url(self):
        return "/" + self.car_id + "/"
    def __str__(self):
        return str(self.id) + ' - ' + str(self.car) + ' ' + str(self.entry_datetime)
    
