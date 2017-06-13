from django.contrib import admin
from .models import car_brand, car_model

admin.site.register(car_brand)
admin.site.register(car_model)