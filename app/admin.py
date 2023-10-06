from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import (
    Style,
    Project,
    Picture,
    User,
    Commentary
)


admin.site.register(Project)
admin.site.register(Picture)
admin.site.register(User, UserAdmin)
admin.site.register(Commentary)
admin.site.register(Style)
