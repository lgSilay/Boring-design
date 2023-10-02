from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from app.forms import CommentForm
from app.models import Style, Project, Commentary


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


def projects_filtered_list_view(request: HttpRequest, pk: int) -> HttpResponse:
    context = {
        "styles": Style.objects.all(),
        "projects": Project.objects.filter(style__id=pk),
    }
    return render(
        request,
        "projects_list.html",
        context=context
    )


def project_detail_view(request: HttpRequest, pk) -> HttpResponse:
    project = Project.objects.get(id=pk)

    if request.method == "GET":
        form = CommentForm(initial={"user": request.user})
        context = {"form": form, "project": project}
        return render(request, "project_detail.html", context=context)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if request.user.is_anonymous:
            form.add_error("content", "Please log in to add a comment")
        elif form.is_valid():
            Commentary.objects.create(
                user=request.user, project=project, **form.cleaned_data
            )
            return HttpResponseRedirect(
                reverse("app:projects_detail", kwargs={"pk": pk})
            )

        context = {"form": form, "project": project}

        return render(request, "project_detail.html", context=context)
