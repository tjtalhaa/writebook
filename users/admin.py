from django.contrib import admin
from . models import Profile
# Register your models here.


class ProfileAdmin (admin.ModelAdmin):
    list_display = ('user',  'image')
    list_display_links = ('user',)
    search_fields = ('user',)
    list_per_page = 25


admin.site.register(Profile, ProfileAdmin)
