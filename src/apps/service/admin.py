from django.contrib import admin
from .models import ServiceModel,CategoryModel,PortfolioModel



@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')
    list_filter = ('name',)
    fieldsets = (
        ('Information', {'fields': ('name','image')}),
        ('Description', {'fields': ('description_about','description_product')}),
    )


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id','service','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_filter = ('service',)
    ordering = ('service',)
    fieldsets = (
        ('Information', {'fields': ('service','name','image')}),
        ('Description', {'fields': ('description',)}),
    )


@admin.register(PortfolioModel)
class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ('id','service','category','name',)
    list_display_links = ('id','name')
    search_fields = ('category','name')
    list_filter = ('category',)
    list_per_page = 20
    fieldsets = (
        ('Information', {'fields': ('service','category','name','description','image')}),
    )
