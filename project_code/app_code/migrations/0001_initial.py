# Generated by Django 3.0 on 2019-12-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_barang', models.IntegerField(default=1)),
                ('nama_barang_col1', models.CharField(max_length=30)),
                ('nama_barang_col2', models.CharField(max_length=30)),
                ('nama_barang_col3', models.CharField(max_length=30)),
                ('gambar_col1', models.CharField(max_length=300)),
                ('gambar_col2', models.CharField(max_length=300)),
                ('gambar_col3', models.CharField(max_length=300)),
            ],
        ),
    ]
