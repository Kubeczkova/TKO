from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = "__all__"


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = "__all__"


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    fields = "__all__"
