# Generated by Django 2.2.4 on 2019-08-02 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190803_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabel_produk',
            name='kode_gudang',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.ref_gudang'),
        ),
    ]
