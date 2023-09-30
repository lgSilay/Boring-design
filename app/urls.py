from django.urls import path

from app.views import (
    index,
    contacts_view,
    projects_list_view,
)

urlpatterns = [
    path("", index, name="index"),
    path("projects/", projects_list_view, name="projects_list"),
    path("contacts/", contacts_view, name="contacts"),
]

app_name = "app"
