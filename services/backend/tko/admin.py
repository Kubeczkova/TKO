from django.contrib import admin

from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'content']

    def has_add_permission(self, request, obj=None):
        return False


    def has_delete_permission(self, request, obj=None):
        return False


    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'author']


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'color']
