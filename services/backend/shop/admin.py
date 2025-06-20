from django.contrib import admin

from shop import models
from shop.models import OrderProduct


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "count"]


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer_name", "created"]
    inlines = [OrderProductInline]