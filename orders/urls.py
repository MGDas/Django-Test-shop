from django.urls import path
from .views import OrderCreate


urlpatterns = [
    path('create/', OrderCreate, name='order_create_url')
]
