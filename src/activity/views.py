#src/activity/views.py
 
from django.shortcuts import render


def activity(request):
	data = {
		'activity_page': 'active',
	}	
	return render(request, 'activity/activity.html', data)
