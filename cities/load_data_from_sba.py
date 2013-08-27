#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import City

import urllib2
import json

# move this out to settings later
JSON_DATA_URL = 'http://api.sba.gov/geodata/city_links_for_state_of/CA.json'

def get_json_from_sba():
	# Returns the JSON from the api.sba.gov url given on test
	sba_json = urllib2.urlopen(JSON_DATA_URL)
	return sba_json

def get_data_from_json(sba_json):
	# returns dictionary of data
	data = json.load(sba_json)
	return data

def enter_city_into_db(city_data):
	# enters a city into the database from a dictionary

	# These two conditionals keep any errors from occuring from
	# None entries into the two fields.
	# Every entry of city_data['description'] is null in the data set
	if city_data['description'] is None:
		city_data['description'] = ''
	# Every entry of city_data['link_title'] is null in the data set
	if city_data['link_title'] is None:
		city_data['link_title'] = ''

	# This script is really just for loading the data initially. So,
	# lets check if the entry is there already and move on if it is.

	"""
		Originally had the commented code below here because I thought 
		feature_id was unique, but it isn't.  There is an entry sharing 
		the same feature_id, name, and pretty much everything except a 
		different url.  Feature_ID: 1525

		So, I'm allowing identical entries and counting on the JSON to be
		accurate.
	"""
	#if City.objects.filter(feature_id=city_data['feature_id']):
		#print 'City already entered in database.'
	#else:
	new_city = City(county_name=city_data['county_name'], 
					description=city_data['description'], 
					feat_class=city_data['feat_class'],
					feature_id=city_data['feature_id'],
					fips_class=city_data['fips_class'],
					fips_county_cd=city_data['fips_county_cd'],
					full_county_name=city_data['full_county_name'],
					link_title=city_data['link_title'],
					url=city_data['url'],
					name=city_data['name'],
					primary_latitude=city_data['primary_latitude'],
					primary_longitude=city_data['primary_longitude'],
					state_abbreviation=city_data['state_abbreviation'],
					state_name=city_data['state_name'])
	print 'Adding', new_city, new_city.state_abbreviation, new_city.feature_id, new_city.primary_latitude, new_city.primary_longitude
	new_city.save()

def enter_cities_into_db(sba_json_data):
	# enters all cities into the database from the url 
	for city in sba_json_data:
		enter_city_into_db(city)

def load_sba():
	"""
		Run this function from the shell to populate the
		database with information from the sba data set
	"""
	enter_cities_into_db(get_data_from_json(get_json_from_sba()))