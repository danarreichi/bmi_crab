from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('orders', views.orders, name='orders'),

    # halaman products
    path('products', views.products, name='products'),
    path('products/add_product', views.add_product, name='add_product'),
    path('products/add_product/save', views.add_product_save, name='add_product_save'),
    path('products/add_satuan', views.add_satuan, name='add_satuan'),
    path('products/add_satuan/save', views.add_satuan_save, name='add_satuan'),
    path('products/add_mutu', views.add_mutu, name='add_mutu'),
    path('products/add_mutu/save', views.add_mutu_save, name='add_mutu_save'),
    path('products/hide_master_mutu/<id_master_mutu>', views.hide_master_mutu, name='hide_master_mutu'),
    path('products/show_master_mutu/<id_master_mutu>', views.show_master_mutu, name='show_master_mutu'),
    path('products/product_detail/<product_id>', views.products_detail, name='products_detail'),
    path('products/product_detail/<product_id>/save', views.update_product, name='update_product_detail'),

    #halaman vendors
    path('vendors', views.vendors, name='vendors'),
    path('vendors/edit_vendor/<vendor_id>', views.edit_vendor, name='vendors_edit'),
    path('vendors/add_vendor', views.add_vendor, name='add_vendor'),
    path('vendors/add_vendor/save', views.add_vendor_save, name='add_vendor_save'),
    path('vendors/edit_vendor/<vendor_id>/save', views.edit_vendor_save, name='edit_vendor_save'),
    path('vendors/daftar_product_vendor/<vendor_id>', views.daftar_product_vendor, name='daftar_product_vendor'),
    path('vendors/daftar_product_vendor/<vendor_id>/add_product', views.vendor_add_product, name='vendor_add_product'),
    path('', views.blank),
]