from django.contrib import admin
from django.contrib.admin import register
from api.models import Yandex, Client, Otzovik


@register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('name', 'slug_name', 'yandex_url', 'google_url', 'otzovik_url', 'double_gis_url')
    prepopulated_fields = {
        'slug_name': ('name',)
    }

# Register your models here.
@register(Otzovik)
class OtzovikAdmin(admin.ModelAdmin):
    fields = ('client', 'raiting', 'count_comments', 'recommend')
    list_display = ('client', 'raiting', 'count_comments', 'create_at', 'recommend')
