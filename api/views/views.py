from django.shortcuts import render
from api.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from loguru import logger



class APIData(APIView):
    def get(self, request):
        urls = None
        data = request.data
        if data.get('token') is None:
            raise 'Error'
        name = data.get('name')
        resurs = f'{name}_url'
        for item in Client._meta.get_fields():
            if item.name == resurs:
                urls: list = [
                    {item['slug_name']:item[resurs]} for item in Client.objects.values(resurs, 'slug_name')
                ]

        if urls is None: return Response(status=500)

        return Response(urls)

    def post(self, request):
        data = request.data
        print(data)
        if not data.get('token'):
            raise 'Error'

        name = data.get('parser')
        data_list = data.get('data')

        for item in data_list:
            for key, value in item.items():
                value['client'] = Client.objects.get(slug_name=key)

                if name == 'otzovik':
                    Otzovik.objects.create(**value)
                elif name == 'yandex':
                    Yandex.objects.create(**value)
                elif name == 'double_gis':
                    DoubleGis.objects.create(**value)


# Create your views here.
        return Response(status=200)