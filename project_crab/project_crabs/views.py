from django.core.checks import messages
from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, Q
from .models import *

# Create your views here.
def blank(request):
    return redirect('/home');

def home(request):
    context = {"home_page":"active"}
    return render(request, 'home/home.html', context)

def dashboard(request):
    context = {"dashboard_page":"active"}
    return render(request, 'home/dashboard.html', context)

def orders(request):
    context = {"orders_page":"active"}
    return render(request, 'home/orders.html', context)

# halaman products
def products(request):
    products_data = Material.objects.values('id_material', 'nama_material', 'status_material', 'id_satuan__nama_satuan').order_by('-status_material', 'nama_material')
    mutu_data = MasterMutu.objects.all()
    context = {"products_page":"active", "mutu_data":mutu_data, "products_data":products_data}
    return render(request, 'home/products.html', context)

def products_detail(request, product_id):
    product_data = Material.objects.get(id_material=product_id)
    satuan_data = SatuanMaterial.objects.all()
    context = {"products_page":"active", "product_data":product_data, "satuan_data":satuan_data}
    return render(request, 'home/products/products_detail.html', context)

def update_product(request, product_id):
    nama_produk = request.POST['nama_produk']
    satuan_produk = request.POST['satuan_produk']
    status_produk = request.POST['status_produk']
    Material.objects.filter(id_material=product_id).update(id_satuan=satuan_produk, nama_material=nama_produk, status_material=status_produk)
    return redirect('/products/product_detail/'+product_id)

def add_product(request):
    satuan_data = SatuanMaterial.objects.all()
    context = {"products_page":"active", "satuan_data":satuan_data}
    return render(request, 'home/products/add_product.html', context)

def add_mutu(request):
    context = {"products_page":"active"}
    return render(request, 'home/products/add_product_mutu.html', context)

def add_satuan(request):
    context = {"products_page":"active"}
    return render(request, 'home/products/add_satuan.html', context)

def add_satuan_save(request):
    nama_satuan = request.POST['nama_satuan']
    SatuanMaterial.objects.create(nama_satuan=nama_satuan)
    return redirect('/products/add_product')
    

def add_mutu_save(request):
    nama_mutu = request.POST['nama_mutu']
    status_mutu = request.POST['status_mutu']
    MasterMutu.objects.create(nama_master_mutu=nama_mutu, status_master_mutu=status_mutu)
    return redirect('/products')

def hide_master_mutu(request, id_master_mutu):
    status_mutu = 0
    MasterMutu.objects.filter(id_master_mutu=id_master_mutu).update(status_master_mutu=status_mutu)
    return redirect('/products')

def show_master_mutu(request, id_master_mutu):
    status_mutu = 1
    MasterMutu.objects.filter(id_master_mutu=id_master_mutu).update(status_master_mutu=status_mutu)
    return redirect('/products')

def add_product_save(request):
    nama_produk = request.POST['nama_produk']
    satuan_produk = request.POST['satuan_produk']
    status_produk = request.POST['status_produk']
    Material.objects.create(id_satuan_id=satuan_produk, nama_material=nama_produk, status_material=status_produk)
    return redirect('/products')

# halaman vendors
def vendors(request):
    vendors_data = Supplier.objects.raw('SELECT sp.ID_SUPPLIER, sp.NAMA_SUPPLIER, lk.NAMA_LOKASI, sp.KODE_SAP, sp.NO_REK, COUNT(DISTINCT dh.ID_MATERIAL) AS JUMLAH_PRODUK FROM supplier sp JOIN lokasi lk ON sp.ID_LOKASI=lk.ID_LOKASI LEFT JOIN detail_harga dh ON sp.ID_SUPPLIER=dh.ID_SUPPLIER GROUP BY sp.ID_SUPPLIER, sp.NAMA_SUPPLIER, lk.NAMA_LOKASI, sp.KODE_SAP, sp.NO_REK ORDER BY count(DISTINCT dh.ID_MATERIAL) DESC')
    context = {"vendors_page":"active", "vendors_data":vendors_data}
    return render(request, 'home/vendors.html', context)

def add_vendor(request):
    lokasi_data = Lokasi.objects.all()
    context = {"vendors_page":"active", "lokasi_data":lokasi_data}
    return render(request, 'home/vendors/add_vendor.html', context)

def add_vendor_save(request):
    lokasi_vendor = request.POST['lokasi_vendor']
    nama_vendor = request.POST['nama_vendor']
    no_sap = request.POST['no_sap']
    no_rek_vendor = request.POST['no_rek_vendor']
    Supplier.objects.create(id_lokasi_id=lokasi_vendor, nama_supplier=nama_vendor, kode_sap=no_sap, no_rek=no_rek_vendor)
    return redirect('/vendors')

def edit_vendor(request, vendor_id):
    lokasi_data = Lokasi.objects.all()
    vendor_data = Supplier.objects.get(id_supplier=vendor_id)
    context = {"vendors_page":"active", "lokasi_data":lokasi_data, "vendor_data":vendor_data}
    return render(request, 'home/vendors/edit_vendor.html', context)

def edit_vendor_save(request, vendor_id):
    lokasi_vendor = request.POST['lokasi_vendor']
    nama_vendor = request.POST['nama_vendor']
    no_sap = request.POST['no_sap']
    no_rek_vendor = request.POST['no_rek_vendor']
    Supplier.objects.filter(id_supplier=vendor_id).update(id_lokasi=lokasi_vendor, nama_supplier=nama_vendor, kode_sap=no_sap, no_rek=no_rek_vendor)
    return redirect('/vendors/edit_vendor/'+vendor_id)

def daftar_product_vendor(request, vendor_id):
    #daftarProduk_data = DetailHarga.objects.values('id_material__nama_material').annotate(jumlah=Count('id_master_mutu')).filter(id_supplier=vendor_id)
    vendor_data = Supplier.objects.get(id_supplier=vendor_id)
    context = {"vendors_page":"active", 
    #"daftarProduk_data":daftarProduk_data,
    "vendor_data":vendor_data}
    return render(request, 'home/vendors/daftar_product_vendor.html', context)

def vendor_add_product(request, vendor_id):
    product_data = Material.objects.filter(status_material=1)
    context = {"vendors_page":"active", "product_data":product_data}
    return render(request, 'home/vendors/add_vendor_product.html', context)