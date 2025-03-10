from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/<str:name>/', views.product, name='product'),
    path('catalog/', views.catalog, name='catalog'),
    path('author/', views.author, name='author'),
    path('contacts/', views.contacts, name='contacts'),
    path('task/<str:years>/<str:century>', views.task_result, name='task_result'),
    path('task/', views.task, name='task'),
]