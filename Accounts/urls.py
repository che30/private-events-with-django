from django.urls import path
from . import views
urlpatterns = [
    path('Register/', views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('add_question/', views.add_question, name='add-question')
]