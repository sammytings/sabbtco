from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


# =========================
# ORDER MODEL
# =========================
class Order(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    order_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    address = models.TextField(blank=True)

    product_name = models.CharField(max_length=255)

    quantity = models.PositiveIntegerField(default=1)

    destination = models.CharField(max_length=255)

    notes = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.order_id:
            random_code = get_random_string(6).upper()
            self.order_id = f"DMK-{random_code}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_id} - {self.full_name}"


# =========================
# BANNER MODEL
# =========================
class Banner(models.Model):

    title = models.CharField(max_length=200, blank=True)

    image = models.ImageField(upload_to="banners/")

    is_active = models.BooleanField(default=True)

    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Banner {self.id}"