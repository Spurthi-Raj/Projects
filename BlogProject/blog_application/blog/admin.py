from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","is_published","created_at")
    list_filter = ("is_published",)
    search_fields = ("title",)

admin.site.register(Post,PostAdmin)
