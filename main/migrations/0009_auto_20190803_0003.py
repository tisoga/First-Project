# Generated by Django 2.2.4 on 2019-08-02 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_ss_produk'),
    ]

    operations = [
        migrations.CreateModel(
            name='ref_gudang',
            fields=[
                ('kode_gudang', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('lokasi_gudang', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tabel_produk',
            name='kode_gudang',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.ref_gudang'),
        ),
    ]
