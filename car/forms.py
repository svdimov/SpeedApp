from django import forms

from car.models import Car


# TODO owner -> This field should remain hidden in forms.
#TODO  place holder to image_ulrs  = "https://..."


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']
        widgets = {
            'image_urls':forms.URLInput(attrs={'placeholder':"https://..."}),
        }

class CarCreateForm(CarBaseForm):
    pass

class CarDetailsForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass

class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
