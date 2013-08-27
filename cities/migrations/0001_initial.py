# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'cities_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('feat_class', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('feature_id', self.gf('django.db.models.fields.IntegerField')()),
            ('fips_class', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fips_county_cd', self.gf('django.db.models.fields.IntegerField')()),
            ('full_county_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link_title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('primary_latitude', self.gf('django.db.models.fields.FloatField')()),
            ('primary_longitude', self.gf('django.db.models.fields.FloatField')()),
            ('state_abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'cities', ['City'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'cities_city')


    models = {
        u'cities.city': {
            'Meta': {'object_name': 'City'},
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feat_class': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_id': ('django.db.models.fields.IntegerField', [], {}),
            'fips_class': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fips_county_cd': ('django.db.models.fields.IntegerField', [], {}),
            'full_county_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'primary_latitude': ('django.db.models.fields.FloatField', [], {}),
            'primary_longitude': ('django.db.models.fields.FloatField', [], {}),
            'state_abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['cities']