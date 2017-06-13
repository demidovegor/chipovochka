"""
Definition of models.
"""

from django.db import models

# Create your models here.


class car_brand(models.Model):
    BrandName = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.BrandName)

class car_model(models.Model):
    BrandName = models.ForeignKey(car_brand)
    ModelName = models.CharField(max_length=100)
    info_v = models.CharField(max_length=100)
    info_type_ebu = models.CharField(max_length=100)
    info_price = models.CharField(max_length=100)
    
    def __unicode__(self):
        return str('asd')