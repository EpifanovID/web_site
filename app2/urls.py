# profileapp/urls.py
from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_me/', views.about_me, name='about_me'),
    path('program/', views.program, name='program'),
    path('management/', views.management, name='management'),
    path('classmates/', views.classmates, name='classmates'),
]
