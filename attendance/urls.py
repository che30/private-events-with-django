from django.urls import path
from . import views
# app_name = 'userevents'
urlpatterns = [
    path('new-attendance/', views.create_attendance_view, name='new-attendance'),
    path('delete/', views.delete_attendance_view, name='delete-attendance')
    # path('events/',views.all_events_view, name='events'),
    # path('<int:event_id>/detail', views.event_detail_view, name='event-detail'),
]