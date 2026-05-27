from django.db import models
from django.contrib.auth.models import User
import random


# ==========================================
# ORDER MODEL
# ==========================================
class Order(models.Model):

    STATUS_CHOICES = [

        ("pending", "Pending"),
        ("processing", "Processing"),
        ("paid", "Paid"),
        ("shipping", "Shipping"),
        ("arrived", "Arrived"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),

    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    order_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    full_name = models.CharField(max_length=255)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    address = models.TextField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    product_name = models.CharField(max_length=255)

    quantity = models.PositiveIntegerField(default=1)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    tracking_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.order_id:

            self.order_id = f"SBT-{random.randint(100000, 999999)}"

        super().save(*args, **kwargs)

    def __str__(self):

        return self.order_id


# ==========================================
# BANNER MODEL
# ==========================================
class Banner(models.Model):

    title = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
        upload_to="banners/"
    )

    is_active = models.BooleanField(
        default=True
    )

    order = models.IntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title or f"Banner {self.id}"


# ==========================================
# ORDER TIMELINE MODEL
# ==========================================
class OrderTimeline(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="timeline"
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-created_at"]

    def __str__(self):

        return f"{self.order.order_id} - {self.title}"


# ==========================================
# DOCUMENT MODEL
# ==========================================
class Document(models.Model):

    order = models.ForeignKey(
        Order,
        related_name="documents",
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=255
    )

    file = models.FileField(
        upload_to="documents/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title


# ==========================================
# PACKAGE PHOTO MODEL
# ==========================================
class PackagePhoto(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    image = models.ImageField(
        upload_to="package_photos/"
    )

    caption = models.CharField(
        max_length=255,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.caption or f"Photo for {self.order.order_id}"