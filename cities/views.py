from .models import City

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from endless_pagination.views import AjaxListView

class NameSearchMixin(object):
	def get_queryset(self):
		# Fetch the queryset from the parent's get_queryset
		queryset = super(NameSearchMixin, self).get_queryset()

		# Get the q GET parameter
		q = self.request.GET.get("q")
		if q:
			# return a filtered queryset
			return queryset.filter(name__icontains=q)
		# No q is specified so we return queryset
		return queryset

class CityListView(LoginRequiredMixin, NameSearchMixin, AjaxListView):
	model = City
	context_object_name = 'object_list'
	
	page_template = 'cities/city_list.html'

class CityDetailView(LoginRequiredMixin, DetailView):
	model = City

class CityUpdateView(LoginRequiredMixin, UpdateView):
	model = City

class CityCreateView(LoginRequiredMixin, CreateView):
	model = City