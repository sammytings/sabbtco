from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "user", "product_name", "quantity", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("order_number", "user__username", "product_name")