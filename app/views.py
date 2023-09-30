from django.shortcuts import render

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
        "projects-list.html",
        context=context
    )