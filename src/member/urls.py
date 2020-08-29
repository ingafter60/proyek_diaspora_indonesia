#src/member/urls.py

from django.urls import path

from src.member import views

urlpatterns = [
	path('', views.member, name='member')
]