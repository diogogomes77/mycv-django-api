from django.contrib import admin

from mycv_django.apps.technologies.models import ParentTechnology, Technology


class ParentTechologyInline(admin.TabularInline):
    model = ParentTechnology
    extra = 1
    fk_name = "parent"


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    inlines = [ParentTechologyInline]
