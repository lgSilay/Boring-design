from django.urls import path

from app.views import (
    index,
    contacts_view,
    projects_list_view,
    projects_filtered_list_view,
    project_detail_view,
)

urlpatterns = [
    path("", index, name="index"),
    path("projects/", projects_list_view, name="projects_list"),
    path("projects/filter/<int:pk>", projects_filtered_list_view, name="projects_filtered_list"),
    path("projects/<int:pk>/", project_detail_view, name="projects_detail"),
    path("contacts/", contacts_view, name="contacts"),
]

app_name = "app"
