from .models import City

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

class CityListView(LoginRequiredMixin, ListView):
	model = City

class CityDetailView(LoginRequiredMixin, DetailView):
	model = City

class CityUpdateView(LoginRequiredMixin, UpdateView):
	model = City

class CityCreateView(LoginRequiredMixin, CreateView):
	model = City