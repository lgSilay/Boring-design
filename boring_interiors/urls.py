from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from app.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls", namespace="app")),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
