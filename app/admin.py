from django.contrib import admin
from .models import Order, Banner, PackagePhoto


# =========================
# PACKAGE PHOTO INLINE
# =========================
class PackagePhotoInline(admin.TabularInline):
    model = PackagePhoto
    extra = 1


# =========================
# ORDER ADMIN
# =========================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "order_id",
        "full_name",
        "phone",
        "product_name",
        "quantity",
        "status",
        "created_at",
    )

    search_fields = (
        "order_id",
        "full_name",
        "phone",
        "product_name",
        "email",
    )

    list_filter = (
        "status",
        "created_at",
    )

    readonly_fields = (
        "order_id",
        "created_at",
    )

    ordering = ("-created_at",)

    inlines = [PackagePhotoInline]


# =========================
# BANNER ADMIN
# =========================
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_active",
        "order",
    )

    list_filter = ("is_active",)

    ordering = ("order",)


# =========================
# PACKAGE PHOTO ADMIN
# =========================
@admin.register(PackagePhoto)
class PackagePhotoAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "caption",
        "uploaded_at",
    )