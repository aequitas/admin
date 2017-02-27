# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinate',
            name='area',
            field=jsonfield.fields.JSONField(default=dict, max_length=10000),
        ),
        migrations.AlterField(
            model_name='coordinate',
            name='geojsontype',
            field=models.CharField(blank=True, choices=[('MultiPolygon', 'MultiPolygon'), ('MultiLineString', 'MultiLineString'), ('MultiPoint', 'MultiPoint'), ('Polygon', 'Polygon'), ('LineString', 'LineString'), ('Point', 'Point')], db_column='geoJsonType', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='isdead',
            field=models.BooleanField(db_column='isDead', default=False, help_text="Dead url's will not be rendered on the map. Scanners can set this check automatically (which might change in the future)"),
        ),
    ]
