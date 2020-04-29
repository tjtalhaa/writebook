from django.contrib import admin
from . models import Post
# Register your models here.


class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author')
    list_display_links = ('title', 'author')
    search_fields = ('title', 'author')
    list_per_page = 25


admin.site.register(Post, PostAdmin)
