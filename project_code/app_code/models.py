from django.db import models

# Create your models here.
class Home(models.Model):
    id_barang = models.IntegerField(default=1)
    nama_barang_col1 = models.CharField(max_length=30, default='')
    nama_barang_col2 = models.CharField(max_length=30, default='')
    nama_barang_col3 = models.CharField(max_length=30, default='')
    gambar_col1 = models.CharField(max_length=300, default='')
    gambar_col2 = models.CharField(max_length=300, default='')
    gambar_col3 = models.CharField(max_length=300, default='')
    harga_barang_col1 = models.CharField(max_length=30, default='')
    harga_barang_col2 = models.CharField(max_length=30, default='')
    harga_barang_col3 = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.nama_barang_col1



