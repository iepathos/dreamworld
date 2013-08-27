from django.conf.urls import patterns, include, url

from .views import CityListView, CityDetailView, CityCreateView, CityUpdateView, City_By_County

urlpatterns = patterns('',
	url(r'^$', CityListView.as_view(), name='city_list'),
	url(r'^(?P<pk>\d+)/$', CityDetailView.as_view(), name='city_detail'),
	url(r'^create/$', CityCreateView.as_view(), name='city_create'),
	url(r'^(?P<pk>\d+)/update/$', CityUpdateView.as_view(), name='city_update'),

	url(r'^by_county/$', City_By_County.as_view(), name='county_view')
)
