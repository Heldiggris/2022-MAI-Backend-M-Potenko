from django.contrib import admin
from spaceapp.models import Planet, Category, User, Atmosphere, StarSystem


# Register your models here.

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Atmosphere)
class AtmosphereAdmin(admin.ModelAdmin):
    pass
    list_display = ('id',)


@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'name')

# admin.site.register(Planet, PlanetAdmin)
# admin.site.register(Category, CategoryAdmin)