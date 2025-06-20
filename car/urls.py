from django.urls import path, include

from car import views

from django.urls import path
from car.views import CatalogView, CreateCarView, DetailCarView, EditCarView, DeleteCarView

urlpatterns = [
    path('catalogue/', CatalogView.as_view(), name='catalogue'),
    path('create/', CreateCarView.as_view(), name='create-car'),
    path('<int:id>/details/', DetailCarView.as_view(), name='car-details'),
    path('<int:id>/edit/', EditCarView.as_view(), name='edit-car'),
    path('<int:id>/delete/', DeleteCarView.as_view(), name='delete-car'),
]



