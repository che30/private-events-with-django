from django.urls import path
from . import views
urlpatterns = [
    path('new-event/', views.create_event_view, name='new-event'),
    path('events/',views.all_events_view, name='events'),
]