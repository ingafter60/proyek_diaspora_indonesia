#src/home/views.py
 
from django.shortcuts import render

from src.home.models import Slider

def index(request):
	sliders = Slider.objects.all()
	data = {
		'sliders':sliders
	}
	return render(request, 'home/index.html', data)
