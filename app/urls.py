from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("quote/", views.quote, name="quote"),
    path("login/", views.login_view, name="login"),
    path("orders/", views.orders, name="orders"),
    path("supplier/register/", views.supplier_register, name="supplier_register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
    'dashboard/order/<int:order_id>/',
    views.update_order,
    name='update_order'
),
    path("dashboard/customers/", views.customers, name="customers"),
    path("dashboard/order/<int:order_id>/", views.update_order, name="update_order"),
    path(
    'orders/<int:order_id>/',
    views.order_detail,
    name='order_detail'
),
    
]