from django.urls import path
from . import views
# app_name = 'userevents'
urlpatterns = [
    path('new-event/', views.create_event_view, name='new-event'),
    path('events/',views.all_events_view, name='events'),
    path('<int:event_id>/detail', views.event_detail_view, name='event-detail'),
]