"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import car_brand, car_model

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def home(request):
    context = {
            'title':'Home Page',
            'year':datetime.now().year,
            'car_brands' : car_brand.objects.all()
        }
    return render(request, 'app/index.html', context)

def about(request):
    context = {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'car_brands' : car_brand.objects.all()
        }
    return render(request, 'app/about.html', context)


def car_models(request):
    context = {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'car_brands' : car_brand.objects.all(),
            'car_models' : car_model.objects.get(ModelName = 'Rio')
        }
    assert isinstance(request, HttpRequest)
    return render(request, 'app/car_models.html', context)