from django.contrib import admin
from .models import ContactModel,ArticleModel,AboutModel,ReviewModel
# Register your models here.

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','job_title','email','is_read','created_at')
    list_display_links = ('id','fullname')
    search_fields = ('fullname','email')
    list_filter = ('is_read','created_at')
    readonly_fields = ('created_at',)
    list_per_page = 20
    fieldsets = (
        ('Information', {'fields': ('fullname','job_title','email','message','is_read')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )


@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','summary','created_at')
    search_fields = ('title',)
    list_filter = ('title','created_at')
    readonly_fields = ('created_at','updated_at')
    list_per_page = 20
    fieldsets = (
        ('Information', {'fields': ('title','content','summary','images')}),
        ('Timestamps', {'fields': ('created_at','updated_at')}),
    )

@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AboutModel.objects.exists():
            return False
        return True
    list_display = ('content','video')
    fieldsets = (
        ('Information', {'fields': ('content','video')}),
    )

@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','feedback')
    search_fields = ('name','feedback')
    list_filter = ('name',)
    list_per_page = 20
    fieldsets = (
        ('Information', {'fields': ('name','feedback','photo','video')}),
    )