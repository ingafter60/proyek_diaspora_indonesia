# diaspora/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from src.home import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name='index'),
   path('activity/', include('src.activity.urls')),
   path('member/', include('src.member.urls')),
   path('group/', include('src.group.urls')),
   path('forum/', include('src.forum.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)