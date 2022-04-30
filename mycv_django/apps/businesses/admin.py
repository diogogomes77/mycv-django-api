from django.contrib import admin

from mycv_django.apps.businesses.models import Business


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    pass
