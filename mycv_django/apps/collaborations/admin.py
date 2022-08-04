from django.contrib import admin

from mycv_django.apps.collaborations.models import Collaboration
from mycv_django.apps.technologies.models import CollaborationTechnology


class CollaborationsInline(admin.TabularInline):
    model = Collaboration
    extra = 1


class CollaborationTechnologyInline(admin.TabularInline):
    model = CollaborationTechnology
    extra = 1


@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    inlines = [CollaborationTechnologyInline]
    list_display = ('id', 'project', 'collaborator')
