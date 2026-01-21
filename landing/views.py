from django.shortcuts import render
from django.views.generic import TemplateView

class Drel1(TemplateView):
    template_name = 'home/d-rel-1.html'
    
class Dtrel1(TemplateView):
    template_name = 'home/dt-rel-1.html'