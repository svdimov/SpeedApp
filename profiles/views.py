from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from profiles.forms import ProfileCreateForm, ProfileUpdateForm, ProfileDetailsForm, ProfileDeleteForm
from profiles.models import Profile
from speedapp.utils import get_user_object


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')
    template_name = 'profiles/profile-create.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_object()






class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return get_user_object()


class ProfileDeliteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')
    form_class =ProfileDeleteForm
    context_object_name = 'profile'


    def get_object(self, queryset=None):
        return get_user_object()

    def form_invalid(self, form):
        return self.form_valid(form)

