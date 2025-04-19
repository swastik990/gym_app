from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.members_view, name='members'),
    path('add/', views.add_member_view, name='add_member'),
    path('edit/<int:member_id>/', views.edit_member_view, name='edit_member'),
    path('delete/<int:member_id>/', views.delete_member_view, name='delete_member'),
    path('subscription/add/<int:member_id>/', views.add_subscription_view, name='add_subscription'),
    path('attendance/mark/<int:member_id>/', views.mark_attendance_view, name='mark_attendance'),
]