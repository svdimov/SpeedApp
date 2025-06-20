from django.db import models


class CarTypeChoices(models.TextChoices):

    Rally = 'Rally', 'Rally'
    Open_wheel = 'Open-wheel', 'Open-wheel'
    Kart = 'Kart', 'Kart'
    Drag = 'Drag', 'Drag'
    Other = 'Other', 'Other'

