from django.db import models

# Create your models here.
class tabel_produk(models.Model):
	kode_produk = models.CharField(max_length = 200, primary_key = True, unique = True)
	nama_produk = models.CharField(max_length = 200)
	stok_produk = models.IntegerField()
	desc_produk = models.TextField()
	harga_produk = models.CharField(max_length = 200)
	foto_produk = models.FileField(upload_to = "images/")


	def __str__(self):
		return self.nama_produk