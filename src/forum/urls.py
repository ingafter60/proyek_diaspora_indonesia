#src/forum/urls.py

from django.urls import path

from src.forum import views

urlpatterns = [
	path('', views.forum, name='forum'),
	path('sub_forum/', views.sub_forum, name='sub_forum'),
	path('topic/', views.topic, name='topic'),
	path('topic_replies/', views.topic_replies, name='topic_replies'),
]