from django.urls import path, re_path
from .views import OrderCreate, AdminOrderDetail, AdminOrderPDF


urlpatterns = [
    path('create/', OrderCreate, name='order_create_url'),
    re_path(r'^admin/order/(?P<order_id>\d+)/$', AdminOrderDetail, name='admin_order_detail_url'),
    re_path(r'^admin/order/(?P<order_id>\d+)/pdf/$', AdminOrderPDF, name='admin_order_pdf_url'),
]
