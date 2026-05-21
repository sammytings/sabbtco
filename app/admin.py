from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "product_name", "quantity", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("full_name", "phone", "product_name", "email")

from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_filter = ("is_active",)
    ordering = ("order",)

from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'full_name',
        'product_name',
        'quantity',
        'status',
        'created_at'
    )

    search_fields = (
        'order_id',
        'full_name',
        'phone',
        'product_name'
    )

    list_filter = ('status', 'created_at')

    readonly_fields = ('order_id', 'created_at')

    ordering = ('-created_at',)