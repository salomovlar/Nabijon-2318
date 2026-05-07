from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="Kitob nomi")
    author = models.CharField(max_length=200, verbose_name="Muallif")
    price = models.IntegerField(verbose_name="Narxi")
    sold = models.BooleanField(default=False, verbose_name="Sotilgan")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
