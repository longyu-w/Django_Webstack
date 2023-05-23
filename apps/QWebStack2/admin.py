from django.contrib import admin

from .models import *


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'titleloader', 'uplloadpage', 'about', 'end', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'icon', ]
    list_display_links = ['name']



@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'parent', ]
    list_display_links = ['name']


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'logo_url','is_show', 'category', ]
    list_display_links = ['url','name']
    list_filter = ('category',)
    search_fields = ['id', 'url', 'logo_url', 'name','is_show', 'category', ]


@admin.register(friendlink)
class friendlinkAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'url', 'is_show', ]
    list_display_links = ['url','name']


