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
    
]