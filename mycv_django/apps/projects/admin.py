from django.contrib import admin

from mycv_django.apps.collaborations.admin import CollaborationsInline
from mycv_django.apps.projects.models import Project
from mycv_django.apps.technologies.models import ProjectTechnology


class ProjectTechologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [CollaborationsInline, ProjectTechologyInline]
