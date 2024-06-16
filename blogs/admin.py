from django.contrib import admin
from .models import Category, Blog, Comment, SocialLink


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "author",
        "status",
        "is_featured",
    )
    search_fields = ("id", "title", "category__category_name", "status")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_featured",)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(SocialLink)
