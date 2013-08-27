from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from core.views import logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
	url(r'^cities/', include('cities.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Login / Logout
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
)
