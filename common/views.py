from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.views.generic import TemplateView

from django.views.generic.edit import BaseFormView

from profiles.forms import ProfileCreateForm
from profiles.models import Profile
from speedapp.utils import get_user_object


class HomePageView(TemplateView):
    model = Profile
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['profile'] = get_user_object()
        return context



