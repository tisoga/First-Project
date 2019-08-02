from django.db import models

# Create your models here.

class ref_gudang(models.Model):
	kode_gudang = models.CharField(max_length = 200, unique=True, primary_key=True)
	lokasi_gudang = models.CharField(max_length = 200)

	def __str__(self):
		return self.kode_gudang	

class tabel_produk(models.Model):
	kode_produk = models.CharField(max_length = 200, primary_key = True, unique = True)
	nama_produk = models.CharField(max_length = 200)
	stok_produk = models.IntegerField()
	desc_produk = models.TextField()
	harga_produk = models.CharField(max_length = 200)
	foto_produk = models.FileField(upload_to = "images/")
	kode_gudang = models.ForeignKey(ref_gudang, default=1, on_delete = models.SET_DEFAULT, blank=True, null=True)

	def __str__(self):
		return self.nama_produk