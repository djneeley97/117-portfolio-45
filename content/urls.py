from django.urls import path
from content import views

urlpatterns = [
    path("", views.projects_list, name="projects_list"),

    path("new/", views.project_new, name="project_new"),
]