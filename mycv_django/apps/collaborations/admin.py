from django.contrib import admin

from mycv_django.apps.collaborations.models import Collaboration


class CollaborationsInline(admin.TabularInline):
    model = Collaboration
    extra = 1
