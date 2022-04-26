from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_developer', 'is_manager')

    def is_developer(self, obj):
        return obj.is_developer

    def is_manager(self, obj):
        return obj.is_manager

    is_developer.boolean = True
    is_developer.short_description = 'Is developer'

    is_manager.boolean = True
    is_manager.short_description = 'Is manager'
