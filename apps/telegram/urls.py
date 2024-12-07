# urls.py
from django.urls import path
from apps.telegram import views


urlpatterns = [
     path('submit_review/', views.submit_review, name='submit_review'),
]
