# Generated by Django 2.2.4 on 2019-08-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190802_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabel_produk',
            name='uang_produk',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
