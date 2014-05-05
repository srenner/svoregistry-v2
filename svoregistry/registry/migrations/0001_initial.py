# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('vin', models.CharField(serialize=False, primary_key=True, unique=True, max_length=17)),
                ('year', models.CharField(blank=True, null=True, max_length=6)),
                ('slappers', models.NullBooleanField(default=False)),
                ('color', models.CharField(blank=True, null=True, max_length=50)),
                ('interior', models.CharField(blank=True, null=True, max_length=50)),
                ('sunroof', models.NullBooleanField(default=False)),
                ('comp_prep', models.NullBooleanField(default=False)),
                ('option_delete', models.NullBooleanField(default=False)),
                ('wing_delete', models.NullBooleanField(default=False, verbose_name='Bi-Wing delete')),
                ('has_23', models.NullBooleanField(default=True, verbose_name='Has 2.3L')),
                ('on_road', models.NullBooleanField(default=True)),
                ('deceased', models.NullBooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('car', models.ForeignKey(to='registry.Car', to_field='vin')),
                ('scrape_id', models.IntegerField(blank=True, null=True)),
                ('year', models.CharField(blank=True, null=True, max_length=6, choices=[('1984', '1984'), ('1985', '1985'), ('1985.5', '1985.5'), ('1986', '1986')])),
                ('slappers', models.NullBooleanField(default=False)),
                ('color', models.CharField(blank=True, null=True, max_length=50, choices=[('1B', '1B (Medium Charcoal)'), ('1C', '1C (Black)'), ('1D', '1D (Dark Gray)'), ('1E', '1E (Silver)'), ('2A', '2A (Medium Canyon Red)'), ('2R', '2R (Jalepeno Red)'), ('4E', '4E (Dark Sage)'), ('7B', '7B (Dark Shadow Blue)'), ('9L', '9L (Oxford White)'), ('9W', '9W (Dark Charcoal)')])),
                ('interior', models.CharField(blank=True, null=True, max_length=50, choices=[('Cloth', 'Cloth'), ('Leather', 'Leather')])),
                ('sunroof', models.NullBooleanField(default=False)),
                ('comp_prep', models.NullBooleanField(default=False)),
                ('option_delete', models.NullBooleanField(default=False)),
                ('wing_delete', models.NullBooleanField(default=False, verbose_name='Bi-Wing delete')),
                ('has_23', models.NullBooleanField(default=True, verbose_name='Has 2.3L')),
                ('on_road', models.NullBooleanField(default=True)),
                ('deceased', models.NullBooleanField(default=False)),
                ('for_sale', models.BooleanField(default=False)),
                ('entry_datetime', models.DateTimeField(verbose_name='Entry Date')),
                ('owner', models.CharField(blank=True, null=True, max_length=255)),
                ('city', models.CharField(blank=True, null=True, max_length=255)),
                ('state', models.CharField(blank=True, null=True, max_length=255, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NT', 'Northwest Territories'), ('NS', 'Nova Scotia'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')])),
                ('country', models.CharField(default='USA', blank=True, null=True, max_length=255, choices=[('USA', 'USA'), ('CA', 'Canada')])),
                ('zipcode', models.CharField(blank=True, null=True, max_length=15)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, null=True, max_length=10000)),
                ('entry_flag', models.IntegerField(default=0, blank=True, null=True)),
                ('photo_height', models.PositiveIntegerField(blank=True, null=True)),
                ('photo_width', models.PositiveIntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, height_field='photo_height', upload_to='photos', null=True, width_field='photo_width')),
                ('ip', models.CharField(default='?', blank=True, null=True, max_length=50)),
                ('geo_lat', models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=8)),
                ('geo_long', models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=8)),
                ('actual_entry_datetime', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
            bases=(models.Model,),
        ),
    ]
