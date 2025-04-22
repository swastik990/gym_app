from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('feedback/', views.submit_feedback_view, name='submit_feedback'),
]