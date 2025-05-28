from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('author/', views.author, name='author'),
    path('feedback_form/', views.feedback_form, name='feedback_form'),
    path('feedback_form/feedback_thanks/', views.feedback_thanks, name='feedback_thanks'),
]
