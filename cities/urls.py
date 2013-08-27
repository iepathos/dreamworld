from django.conf.urls import patterns, include, url

from .views import CityListView, CityDetailView, CityCreateView, CityUpdateView

urlpatterns = patterns('',
	url(r'^$', CityListView.as_view(), name='city_list'),
	url(r'^(?P<pk>\d+)/$', CityDetailView.as_view(), name='city_detail'),
	url(r'^create/$', CityCreateView.as_view(), name='city_create'),
	url(r'^(?P<pk>\d+)/update/$', CityUpdateView.as_view(), name='city_update'),
)
