from django.urls import path 
from apps.settings.views import index ,menu,about,contact


urlpatterns = [
    path('', index, name='index'),
    path('menu', menu, name='menu'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]