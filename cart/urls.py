from django.urls import path, re_path
from .views import (
	CartRemove, CartDetail, CartAdd
)


urlpatterns = [
    re_path(r'^remove/(?P<product_id>\d+)/$', CartRemove, name='cart_remove_url'),
    re_path(r'^add/(?P<product_id>\d+)/$', CartAdd, name='cart_add_url'),
    re_path(r'^$', CartDetail, name='cart_detail_url'),
]
