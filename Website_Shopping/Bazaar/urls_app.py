from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('login', views.login_user, name="Login"),
    path('register', views.register, name="Register"),
    path('clothing', views.clothing, name="Clothing"),
    path('footwear', views.footwear, name="FootWear"),
    path('skincare', views.skincare, name="SkinCare"),
    path('prod_view', views.product_view, name="Product_View"),
    path('payments', views.payment_page, name="Payment"),
    path('success', views.success, name="Success"),
    path('orders_view', views.orders_view, name="Orders_View"),
    path('pending_payments', views.pending_payments, name="Pending_payments"),
    path('delete', views.delete, name="Delete")
]