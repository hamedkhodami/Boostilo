from django.contrib import admin
from .models import ProfileTeam


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


