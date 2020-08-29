#src/group/urls.py

from django.urls import path

from src.group import views

urlpatterns = [
	path('', views.group, name='group')
]