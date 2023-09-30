from django.shortcuts import render
from django.views import generic

from app.models import Style, Project


def index(request):
    return render(request, "index.html")


def contacts_view(request):
    return render(request, "contacts.html")


def projects_list_view(request):
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
