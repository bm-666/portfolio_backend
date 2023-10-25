from rest_framework.views import APIView
from rest_framework.response import Response, SimpleTemplateResponse

from api.models import Client
from loguru import logger
import json
from datetime import date
class AllClients(APIView):
    template = 'all_clients.html'
    def get(self, request):
        clients = list(Client.objects.all())
        context = {
            'clients': clients
        }
        return SimpleTemplateResponse(template=self.template, context=context)

class ClientDetail(APIView):
    template = 'client_detail.html'
    def get(self, request, slug_name):
        client = Client.objects.get(slug_name=slug_name)
        client_stat: dict = {
        }

        client_stat['name'] = client.name
        client_stat['otzovik'] = client.otzovik_set.last()
        client_stat['yandex'] = client.yandex_set.last()
        client_stat['google'] = client.googlemaps_set.last()
        client_stat['gis'] = client.doublegis_set.last()
        return  SimpleTemplateResponse(template=self.template, context=client_stat)
