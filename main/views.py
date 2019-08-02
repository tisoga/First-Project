from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import form_produk
from .models import tabel_produk
# Create your views here.
def homepage(request):
	if request.method == 'POST':
		logout(request)
	return render(request = request,
				  template_name = 'main/homepage.html',
				  context = {'active': "home"})

def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save();
			username = form.cleaned_data['username']
			messages.success(request, f"Username {username.title()} berhasil registrasi")
			login(request, user)
			return redirect('main:homepage')
	return render(request = request,
				  template_name = 'main/register.html',
				  context = {'form':form , 
				  			 'active': 'register'})

def login_request(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username = username, password = password)
			messages.info(request, f"Username {username.title()} Berhasil Login")
			login(request, user)
			return redirect('main:homepage')

	return render(request = request,
				  template_name = 'main/login_page.html',
				  context = {'form':form ,
				  			 'active': 'login'})
def logout_request(request):
	logout(request)
	messages.success(request, f"Success Logout")
	return redirect('main:homepage')

def tambah_produk(request):
	form = form_produk()
	if request.method == 'POST':
		form = form_produk(request.POST, request.FILES)
		if form.is_valid():
			kode = form.cleaned_data['kode_produk']
			nama = form.cleaned_data['nama_produk']
			stok = form.cleaned_data['stok_produk']
			desc = form.cleaned_data['desc_produk']
			harga = form.cleaned_data['harga_produk']
			foto = form.cleaned_data['foto_produk']
			tabel_produk.objects.create(kode_produk = kode, nama_produk = nama,
								  		stok_produk = stok, desc_produk = desc,
								  		harga_produk = harga, foto_produk = foto)
			messages.success(request, f"Produk {nama.title()} berhasil disimpan!")
			return redirect('main:lihat')
	return render(request = request,
				  template_name = 'main/tambah_produk.html',
				  context = {'form': form,
				             'active': 'tambah'})

def lihat_produk(request):
	tabel = tabel_produk.objects.all()
	if request.GET.get('kode'):
		kode = request.GET.get('kode')
		hapus = tabel_produk.objects.get(kode_produk = kode)
		print(hapus)
		hapus.delete()
		messages.success(request, f"Produk {hapus} Berhasil Dihapus")
		return redirect('main:lihat')
	return render(request = request,
				  template_name = 'main/lihat_produk.html',
				  context = {'tabel': tabel,
				  			 'active': "lihat"})

def lihat_detail(request):
	if request.GET.get('kode'):
		kode = request.GET.get('kode')
		produk = tabel_produk.objects.get(kode_produk = kode)
		print('test')
		return render(request = request,
			    	  template_name = 'main/lihat_detail.html',
			    	  context = {'produk': produk,
			    	  			 'active': 'lihat'})
	elif request.GET.get('edit'):
		kode = request.GET.get('edit')
		produk = tabel_produk.objects.get(kode_produk = kode)
		initial = {'kode_produk': produk.kode_produk,
				   'nama_produk': produk.nama_produk,
				   'stok_produk': produk.stok_produk,
				   'desc_produk': produk.desc_produk,
				   'harga_produk': produk.harga_produk}
		form = form_produk(initial = initial)
		if request.method == 'POST':
			form = form_produk(request.POST, request.FILES)
			if form.is_valid():
				# kodeu = form.cleaned_data['kode_produk']
				# nama = form.cleaned_data['nama_produk']
				# stok = form.cleaned_data['stok_produk']
				# desc = form.cleaned_data['desc_produk']
				# harga = form.cleaned_data['harga_produk']
				# foto = form.cleaned_data['foto_produk']
				# tabel_produk.objects.filter(kode_produk = kode).insert(nama_produk = nama,
				# 													   stok_produk = stok,
				# 													   desc_produk = desc,
				# 													   harga_produk = harga,
				# 													   foto_produk = foto)
				kodeu = request.POST.get('kode_produk')
				nama = request.POST.get('nama_produk')
				stok = request.POST.get('stok_produk')
				desc = request.POST.get('desc_produk')
				harga = request.POST.get('harga_produk')
				foto = request.FILES.get('foto_produk')
				update = tabel_produk.objects.get(kode_produk = kode)
				update.nama_produk = nama
				update.stok_produk = stok
				update.desc_produk = desc
				update.harga_produk = harga
				update.foto_produk = foto
				update.save()
				messages.success(request, f"Produk {nama} Berhasil di ubah")
				return redirect('main:lihat')
			else:
				print('asa')
		return render(request = request,
					  template_name = 'main/lihat_detail.html',
					  context = {'form': form,
					  			 "active": 'lihat',
					  			 'produk': produk})