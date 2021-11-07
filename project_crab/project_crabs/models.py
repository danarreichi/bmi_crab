# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Material(models.Model):
    id_material = models.AutoField(db_column='ID_MATERIAL', primary_key=True)  # Field name made lowercase.
    id_satuan = models.ForeignKey('SatuanMaterial', models.DO_NOTHING, db_column='ID_SATUAN', blank=True, null=True)  # Field name made lowercase.
    nama_material = models.CharField(db_column='NAMA_MATERIAL', max_length=255)  # Field name made lowercase.
    status_material = models.IntegerField(db_column='STATUS_MATERIAL', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.id_material

    def id_satuan_str(self):
        return self.id_satuan.__str__()

    class Meta:
        db_table = 'material'


class MasterMutu(models.Model):
    id_master_mutu = models.AutoField(db_column='ID_MASTER_MUTU', primary_key=True)
    nama_master_mutu = models.CharField(db_column='NAMA_MASTER_MUTU', max_length=255)
    status_master_mutu = models.IntegerField(db_column='STATUS_MASTER_MUTU', blank=True, null=True)

    def __str__(self):
        return self.id_master_mutu

    class Meta:
        db_table = 'master_mutu'


class ProdukSupplier(models.Model):
    id_produk_supplier = models.AutoField(db_column='ID_PRODUK_SUPPLIER', primary_key=True)  # Field name made lowercase.
    id_material = models.ForeignKey(Material, models.DO_NOTHING, db_column='ID_MATERIAL', blank=True, null=True)  # Field name made lowercase.
    id_supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='ID_SUPPLIER', blank=True, null=True)  # Field name made lowercase.
    status_aktif = models.IntegerField(db_column='STATUS_AKTIF')  # Field name made lowercase.

    def __str__(self):
        return self.id_produk_supplier

    class Meta:
        db_table = 'produk_supplier'


class DetailHarga(models.Model):
    id_detail_harga = models.AutoField(db_column='ID_DETAIL_HARGA', primary_key=True)  # Field name made lowercase.
    id_master_mutu = models.ForeignKey(MasterMutu, models.DO_NOTHING, db_column='ID_MASTER_MUTU', blank=True, null=True)  # Field name made lowercase.
    id_produk_supplier = models.ForeignKey(ProdukSupplier, models.DO_NOTHING, db_column='ID_PRODUK_SUPPLIER', blank=True, null=True)  # Field name made lowercase.
    tanggal = models.DateField(db_column='TANGGAL')  # Field name made lowercase.
    harga = models.DecimalField(db_column='HARGA', max_digits=11, decimal_places=2)  # Field name made lowercase.

    def __str__(self):
        return self.id_detail_harga

    class Meta:
        db_table = 'detail_harga'


class Lokasi(models.Model):
    id_lokasi = models.AutoField(db_column='ID_LOKASI', primary_key=True)  # Field name made lowercase.
    nama_lokasi = models.CharField(db_column='NAMA_LOKASI', max_length=255)  # Field name made lowercase.
    status_lokasi = models.IntegerField(db_column='STATUS_LOKASI')  # Field name made lowercase.

    def __str__(self):
        return self.id_lokasi

    class Meta:
        db_table = 'lokasi'


class Receiving(models.Model):
    no_receiving = models.CharField(db_column='NO_RECEIVING', primary_key=True, max_length=10)  # Field name made lowercase.
    id_detail_harga = models.ForeignKey(DetailHarga, models.DO_NOTHING, db_column='ID_DETAIL_HARGA', blank=True, null=True)  # Field name made lowercase.
    id_user = models.ForeignKey('UserBmi', models.DO_NOTHING, db_column='ID_USER', blank=True, null=True)  # Field name made lowercase.
    tanggal_terima = models.DateField(db_column='TANGGAL_TERIMA')  # Field name made lowercase.
    jumlah_berat = models.DecimalField(db_column='JUMLAH_BERAT', max_digits=10, decimal_places=0)  # Field name made lowercase.

    def __str__(self):
        return self.no_receiving

    class Meta:
        db_table = 'receiving'


class SatuanMaterial(models.Model):
    id_satuan = models.AutoField(db_column='ID_SATUAN', primary_key=True)  # Field name made lowercase.
    nama_satuan = models.CharField(db_column='NAMA_SATUAN', max_length=255)  # Field name made lowercase.

    def __str__(self):
        return self.id_satuan

    class Meta:
        db_table = 'satuan_material'


class Supplier(models.Model):
    id_supplier = models.AutoField(db_column='ID_SUPPLIER', primary_key=True)  # Field name made lowercase.
    id_lokasi = models.ForeignKey(Lokasi, models.DO_NOTHING, db_column='ID_LOKASI', blank=True, null=True)  # Field name made lowercase.
    nama_supplier = models.CharField(db_column='NAMA_SUPPLIER', max_length=255)  # Field name made lowercase.
    kode_sap = models.CharField(db_column='KODE_SAP', max_length=10)  # Field name made lowercase.
    no_rek = models.CharField(db_column='NO_REK', max_length=255)  # Field name made lowercase.

    def __str__(self):
        return self.id_supplier

    def id_lokasi_str(self):
        return self.id_lokasi.__str__()

    def nama_supplier_substr_6(self):
        return self.nama_supplier[:6]

    class Meta:
        db_table = 'supplier'


class UserBmi(models.Model):
    id_user = models.CharField(db_column='ID_USER', primary_key=True, max_length=10)  # Field name made lowercase.
    nama_user = models.CharField(db_column='NAMA_USER', max_length=255)  # Field name made lowercase.
    
    def __str__(self):
        return self.id_user
    
    class Meta:
        db_table = 'user_bmi'