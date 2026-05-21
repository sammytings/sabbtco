from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .models import Banner

def index(request):
    banners = Banner.objects.filter(is_active=True).order_by("order")

    # fallback images if admin hasn't added any
    default_banners = [
        "static/images/banner1.jpg",
        "static/images/banner2.jpg",
    ]

    context = {
        "banners": banners,
        "default_banners": default_banners,
    }
    return render(request, "index.html", context)

def services(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")

from .models import Order
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required

def quote(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        product = request.POST.get("product")
        qty = request.POST.get("qty")
        notes = request.POST.get("notes")

        # Save to database
        Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=name,
            email=email,
            phone=phone,
            address="Not provided",
            product_name=product,
            quantity=qty if qty else 1,
            notes=notes
        )

        messages.success(request, "Your quote request has been submitted successfully!")
        return redirect("orders")  # go to orders page

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
from .forms import OrderForm
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def orders(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            messages.success(request, "Order placed successfully!")
            return redirect("orders")  # redirect back to orders page
    else:
        form = OrderForm()

    # show only logged in user's orders
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "orders.html", {
        "form": form,
        "orders": orders
    })
def supplier_register(request):
    return render(request, "supplier_register.html")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order



def dashboard(request):

    total_orders = Order.objects.count()

    pending_orders = Order.objects.filter(
        status="pending"
    ).count()

    shipped_orders = Order.objects.filter(
        status="shipped"
    ).count()

    delivered_orders = Order.objects.filter(
        status="delivered"
    ).count()

    recent_orders = Order.objects.order_by(
        "-created_at"
    )[:10]

    context = {
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "shipped_orders": shipped_orders,
        "delivered_orders": delivered_orders,
        "recent_orders": recent_orders,
    }

    return render(request, "dashboard/index.html", context)