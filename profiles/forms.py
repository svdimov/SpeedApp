from django import forms
from django.views.generic import CreateView

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age' , 'password']
        widgets = {
            'password': forms.PasswordInput(

            ),
        }

class ProfileDetailsForm(ProfileBaseForm):
    pass


class ProfileUpdateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(

            ),
        }


class ProfileDeleteForm(ProfileBaseForm):
    pass
