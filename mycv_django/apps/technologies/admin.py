from django.contrib import admin

from mycv_django.apps.technologies.models import ParentTechnology, Technology


class ParentTechologyInline(admin.TabularInline):
    model = ParentTechnology
    extra = 1
    fk_name = "parent"


class TechologyInline(admin.TabularInline):
    model = Technology
    extra = 1


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    inlines = [ParentTechologyInline]
    prepopulated_fields = {"slug": ("name",)}
