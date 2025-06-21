

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from car.forms import CarCreateForm, CarEditForm, CarDeleteForm
from car.models import Car
from speedapp.utils import get_user_object


# Create your views here.



class CatalogView(ListView):
    model = Car
    template_name = 'catalogue.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context

class CreateCarView(CreateView):
    model = Car
    form_class = CarCreateForm
    success_url = reverse_lazy('catalogue')
    template_name = 'car/car-create.html'



    def form_valid(self, form):
        form.instance.owner = get_user_object()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()  # Тук се подава профилът
        return context


class DetailCarView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()  # Тук се подава профилът
        return context

class EditCarView(UpdateView):
    model = Car
    template_name = 'car/car-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')
    form_class = CarEditForm



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()  # Тук се подава профилът
        return context


class DeleteCarView(DeleteView):
    model = Car
    template_name = 'car/car-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')
    form_class = CarDeleteForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()  # Тук се подава профилът
        return context
