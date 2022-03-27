from django.contrib import admin
from spaceapp.models import Planet, Category


# Register your models here.

# @admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Planet, PlanetAdmin)
# admin.site.register(Category, CategoryAdmin)