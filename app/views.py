from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from app.models import Style, Project


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def contacts_view(request: HttpRequest) -> HttpResponse:
    return render(request, "contacts.html")


def projects_list_view(request: HttpRequest) -> HttpResponse:
    context = {
        "styles": Style.objects.all(),
        "projects": Project.objects.all(),
    }
    return render(
        request,
        "projects_list.html",
        context=context
    )


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = "project_detail.html"
