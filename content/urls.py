from django.urls import path
from content import views

urlpatterns = [
    path("", views.projects_list, name="projects_list"),
]