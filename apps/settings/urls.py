from django.urls import path 
from apps.settings.views import index ,menu,about,contact,single_blog,elements,you


urlpatterns = [
    path('', index, name='index'),
    path('menu', menu, name='menu'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('blog',single_blog,name='blog'),
    path('elements',elements,name='elements'),
    path('you',you,name='you'),
]