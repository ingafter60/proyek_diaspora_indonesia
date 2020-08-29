#src/member/views.py
 
from django.shortcuts import render


def member(request):
	data = {
		'member_page': 'active',
	}	
	return render(request, 'member/member.html', data)
