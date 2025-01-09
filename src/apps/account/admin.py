from django.contrib import admin
from .models import ProfileTeam,ClientModel

# Register your models here.

@admin.register(ProfileTeam)
class ProfileTeamAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','role')
    list_display_links = ('id','fullname')
    search_fields = ('fullname','role')
    list_filter = ('role','created_at')
    readonly_fields = ('created_at','updated_at')
    list_per_page = 20
    fieldsets = (
        ('Information', {'fields': ('user','fullname','role','bio','photo')}),
        ('Timestamps', {'fields': ('created_at','updated_at')}),
    )

@admin.register(ClientModel)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','jobs','email','created_at')
    list_display_links = ('id','fullname')
    search_fields = ('fullname','jobs','email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    list_per_page = 20
    fieldsets = (
        ('Information', {'fields': ('fullname','jobs','email')}),
        ('Registration Date', {'fields': ('created_at',)}),
    )
