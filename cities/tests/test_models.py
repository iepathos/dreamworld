import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from cities.models import City

class CityTests(TestCase):
	def setUp(self):
		City.objects.get_or_create(county_name='A County Name', 
								description='A City description - probably null', 
								feat_class='A Feat Class',
								feature_id='1',
								fips_class='A Fips Class',
								fips_county_cd='2',
								full_county_name='A Full County Name',
								link_title='A Title to a link - probably null',
								url='http://google.com',
								name='A City Name',
								primary_latitude='30',
								primary_longitude='40',
								state_abbreviation='CA',
								state_name='California')

	def test_create(self):
		test_city = City(name='Another City Name')
		self.assertEquals(test_city.name='Another City Name')

	def test_update(self):
		test_city = City.objects.get(name='A City Name')
		new_city_name = 'A New City Name'
		test_city.name=new_city_name
		test_city.save()
		self.assertEquals(test_city.name, new_city_name)

	def test_delete(self):
		test_city = City.objects.get(name='A City Name')
		self.assertEquals(City.objects.count(), 1)
		test_city.delete()
		self.assertEquals(City.objects.count(), 0)