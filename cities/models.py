from django.db import models

class City(models.Model):
	county_name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	feat_class = models.CharField(max_length=200)
	feature_id = models.IntegerField()
	fips_class = models.CharField(max_length=50)
	fips_county_cd = models.IntegerField()
	full_county_name = models.CharField(max_length=200)
	link_title = models.CharField(blank=True)
	url = models.URLField(max_lenght=255, blank=True)
	name = models.CharField(max_length=200)
	primary_latitude = models.FloatField()
	primary_longitude = models.FloatField()
	state_abbreviation = models.CharField(max_length=2)
	state_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name, self.state_abbreviation

	class Meta:
		verbose_name = 'City'
		verbose_name_plural = 'Cities'