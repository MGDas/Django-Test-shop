from django.urls import path, re_path
from .views import (
	ProductList, ProductDetail
)


urlpatterns = [
    re_path(r'^(?P<category_slug>[-\w]+)/$', ProductList, name='product_list_url'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProductDetail, name='product_detail_url'),
    re_path(r'^$', ProductList, name='product_list_url'),
]
