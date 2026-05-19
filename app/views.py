from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")

def quote(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        country = request.POST.get("country")
        product = request.POST.get("product")
        qty = request.POST.get("qty")
        shipping = request.POST.get("shipping")
        notes = request.POST.get("notes")

        messages.success(request, "Your quote request has been submitted successfully!")
        return redirect("quote")

    return render(request, "quote.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("login")

    return render(request, "login.html")

from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def orders(request):
    user_orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders.html", {"orders": user_orders})

def supplier_register(request):
    return render(request, "supplier_register.html")