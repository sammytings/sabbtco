from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .models import Banner
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.contrib.auth.models import User

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

from django.shortcuts import render, redirect
from .models import Order


from .models import Order

@login_required
def orders(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        product_name = request.POST.get("product_name")
        quantity = request.POST.get("quantity")
        amount = request.POST.get("amount")

        notes = request.POST.get("notes")

        Order.objects.create(

            user=request.user,

            full_name=full_name,
            email=email,
            phone=phone,
            address=address,

            product_name=product_name,
            quantity=quantity,
            amount=amount,

            notes=notes

        )

    user_orders = Order.objects.filter(user=request.user)

    return render(request, "orders.html", {
        "orders": user_orders
    })

    return render(request, "quote.html")

def supplier_register(request):
    return render(request, "supplier_register.html")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Order


@staff_member_required
def dashboard(request):

    orders = Order.objects.all().order_by("-created_at")

    context = {

        "orders": orders

    }

    return render(
        request,
        "dashboard/index.html",
        context
    )

from django.shortcuts import get_object_or_404, redirect


@staff_member_required
def update_order(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":

        order.status = request.POST.get("status")

        order.tracking_number = request.POST.get("tracking")

        order.save()

        return redirect("admin_dashboard")

    context = {

        "order": order

    }

    return render(
        request,
        "adminpanel/update_order.html",
        context
    )

from django.contrib.auth.decorators import login_required


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "orders/my_orders.html",
        {"orders": orders}
    )

def track_order(request):

    order = None

    query = request.GET.get("order_id")

    if query:

        order = Order.objects.filter(
            order_id=query
        ).first()

    return render(
        request,
        "orders/track.html",
        {"order": order}
    )

def customers(request):

    customers = User.objects.all().order_by("-date_joined")

    return render(request, "dashboard/customers.html", {
        "customers": customers
    })

def update_order(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":

        order.status = request.POST.get("status")
        order.notes = request.POST.get("notes")

        order.save()

        return redirect("dashboard")

    return render(request, "dashboard/update_order.html", {
        "order": order
    })

from django.shortcuts import render, get_object_or_404
from app.models import Order


def order_detail(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id
    )

    timeline = order.timeline.all()

    context = {
        "order": order,
        "timeline": timeline,
    }

    return render(
        request,
        "dashboard/order_detail.html",
        context
    )