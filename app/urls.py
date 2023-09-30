from django.urls import path

from app.views import index, contacts_view

urlpatterns = [
    path("", index, name="index"),
    path("contacts/", contacts_view, name="contacts")
]

app_name = "app"
