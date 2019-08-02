from django import forms
from .models import ref_gudang

gudang = ref_gudang.objects.all()
choices = []
for x in gudang:
	choices.append([x,x])

class form_produk(forms.Form):
	kode_produk = forms.CharField()
	nama_produk = forms.CharField()
	stok_produk = forms.IntegerField(min_value = 0)
	desc_produk = forms.CharField(widget = forms.Textarea)
	harga_produk = forms.IntegerField(min_value = 0)
	foto_produk = forms.FileField()
	# lokasi_gudang = forms.ChoiceField(choices = choices)