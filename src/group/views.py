#src/group/views.py
 
from django.shortcuts import render


def group(request):
	data = {
		'group_page': 'active',
	}	
	return render(request, 'group/group.html', data)
