#src/activity/urls.py

from django.urls import path

from src.activity import views

urlpatterns = [
	path('', views.activity, name='activity')
]