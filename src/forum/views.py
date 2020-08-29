#src/forum/views.py
 
from django.shortcuts import render


def forum(request):
	data = {
		'forum_page': 'active',
	}	
	return render(request, 'forum/forum.html', data)

def sub_forum(request):
	data = {
		'sub_forum_page': 'active',
	}	
	return render(request, 'forum/sub_forum.html', data)

def topic(request):
	data = {
		'topic_page': 'active',
	}	
	return render(request, 'forum/topics.html', data)

def topic_replies(request):
	data = {
		'topic_replies_page': 'active',
	}	
	return render(request, 'forum/topic_replies.html', data)
