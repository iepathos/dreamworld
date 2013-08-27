from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
	#fields = ( 'name', 'state_abbreviation', 'primary_latitude', 'primary_longitude' )
	list_display = ('name', 'state_abbreviation', 'primary_latitude', 'primary_longitude' )
admin.site.register(City, CityAdmin)