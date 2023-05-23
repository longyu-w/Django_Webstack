from django.contrib import admin

from .models import *


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'titleloader', 'uplloadpage', 'about', 'end', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'icon', ]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'parent', ]


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'url', 'logo_url', 'name', 'describtion', 'is_show', 'category', ]


@admin.register(friendlink)
class friendlinkAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'url', 'is_show', ]

