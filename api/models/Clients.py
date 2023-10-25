from django.db import models
from django.shortcuts import reverse




class Client(models.Model):
    name = models.CharField(max_length=1000)
    slug_name = models.SlugField(unique=True, max_length=1000)
    yandex_url = models.CharField(max_length=5000, null=True, blank=True, verbose_name='ЯндексКарты')
    google_url = models.CharField(max_length=5000, null=True, blank=True, verbose_name='GoogleMaps')
    double_gis_url = models.CharField(max_length=5000, null=True, blank=True, verbose_name='2Gis')
    otzovik_url = models.CharField(max_length=5000, null=True, blank=True, verbose_name='Отзовик')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"clients/{self.slug_name}"
    class Meta:
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

