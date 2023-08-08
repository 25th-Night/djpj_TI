from django.urls import path, re_path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.ProductListView.as_view(), name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
]