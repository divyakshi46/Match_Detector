from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page to display the form
    path('check/', views.check, name='check'),  # URL to handle form submission and show result
]