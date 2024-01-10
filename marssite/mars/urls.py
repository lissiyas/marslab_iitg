from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='mars_home'),
    path('people/',views.people, name ='people'),
    path('alumni/',views.alumni, name ='alumni'),
    path('infrastructure/',views.infrastructure, name ='infrastructure'),
    path('research/',views.research, name ='research'),
    path('publications/',views.publications, name ='publications'),
    path('news/',views.news, name ='news'),
    path('gallery/',views.gallery, name ='gallery'),
    path('video/',views.video, name ='video'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    