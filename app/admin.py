from django.contrib import admin
from django.contrib.auth.models import Group

from app.models import (
    Style,
    Project,
    Picture,
    User,
    Commentary
)

# admin.site.unregister(Group)
admin.site.register(Project)
admin.site.register(Picture)
admin.site.register(User)
admin.site.register(Commentary)
admin.site.register(Style)

