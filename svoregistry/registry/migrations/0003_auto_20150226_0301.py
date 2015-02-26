# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_entry_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='list_price',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=9),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='transaction_price',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=9),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='color',
            field=models.CharField(null=True, blank=True, max_length=50, choices=[('1B', '1B (Medium Charcoal)'), ('1C', '1C (Black)'), ('1D', '1D (Dark Gray)'), ('1E', '1E (Silver)'), ('2A', '2A (Medium Canyon Red)'), ('2R', '2R (Jalepeno Red)'), ('4E', '4E (Dark Sage)'), ('7B', '7B (Dark Shadow Blue)'), ('9L', '9L (Oxford White)'), ('9W', '9W (Dark Charcoal)'), ('', 'Unknown or Custom')]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='country',
            field=models.CharField(null=True, blank=True, default='USA', max_length=255, choices=[('USA', 'USA'), ('CA', 'Canada'), ('', 'Other Country')]),
        ),
    ]
