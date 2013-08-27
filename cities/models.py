from django.db import models

class City(models.Model):
	# Model based directly off of the JSON found at 
	# http://api.sba.gov/geodata/city_links_for_state_of/CA.json

	county_name = models.CharField(max_length=200)
	description = models.TextField(blank=True) 
	# JSON has description set to null, but in Django its considered 
	# bad form to store a TextField, CharField, EmailField and a few 
	# others with null=true, so just set to Blank
	
	feat_class = models.CharField(max_length=200)
	feature_id = models.IntegerField()
	fips_class = models.CharField(max_length=50)
	fips_county_cd = models.IntegerField()
	full_county_name = models.CharField(max_length=200)
	link_title = models.CharField(max_length=200, blank=True)
	url = models.URLField(max_length=255, blank=True)
	name = models.CharField(max_length=200)
	primary_latitude = models.FloatField()
	primary_longitude = models.FloatField()
	state_abbreviation = models.CharField(max_length=2)
	state_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'City'
		verbose_name_plural = 'Cities'