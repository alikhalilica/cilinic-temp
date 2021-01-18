from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact_view, name='contact'),
    path('about', views.about_view, name='about'),
    path('privacy', views.privacy, name='privacy'),
    path('rules', views.rules, name='rules'),
    
]
