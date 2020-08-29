#src/activity/views.py
 
from django.shortcuts import render


def index(request):
	return render(request, 'activity/activity.html')
