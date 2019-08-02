from django import forms

class form_produk(forms.Form):
	kode_produk = forms.CharField()
	nama_produk = forms.CharField()
	stok_produk = forms.IntegerField(min_value = 0)
	desc_produk = forms.CharField(widget = forms.Textarea)
	harga_produk = forms.IntegerField(min_value = 0)
	foto_produk = forms.FileField()