from django.contrib import admin

from . import models


@admin.register(models.Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass
