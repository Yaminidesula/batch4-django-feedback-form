from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
]
