from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index),
    path("projects", views.projects),
    path("imprint", views.imprint)
]