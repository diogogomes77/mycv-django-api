from django.contrib import admin

from mycv_django.apps.collaborations.admin import CollaborationsInline
from mycv_django.apps.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [CollaborationsInline]
