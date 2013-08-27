from django.conf.urls import patterns, include, url

from .views import CityListView, CityDetailView

urlpatterns = patterns('',
	url(r'^$', CityListView.as_view(), name='city_list'),
	url(r'^(?P<pk>\d+)/$', CityDetailView.as_view(), name='city_detail'),
)
