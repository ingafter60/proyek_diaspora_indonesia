# diaspora/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from src.home import views
from src.activity import views 

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name='index'),
   path('activity/', views.index, name='index_activity'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)