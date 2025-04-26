from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('create-category/', views.create_category_view, name='create_category'),  # Add this line
]