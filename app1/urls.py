from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('author/', views.author, name='author'),
    path('feedback_form/', views.feedback_form, name='feedback_form'),
    path('feedback_form/feedback_thanks/', views.feedback_thanks, name='feedback_thanks'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),
]
