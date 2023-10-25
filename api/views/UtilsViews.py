from api.models import Client
from datetime import datetime


class DataClientModels:
    @staticmethod
    def get_all_data_resurs(resurs, slug_name):
        if resurs == 'yandex':
            data = Client.objects.get(slug_name=slug_name).yandex_set.all()
        elif resurs == 'google':
            data = Client.objects.get(slug_name=slug_name).googlemaps_set.all()
        elif resurs == 'double_gis':
            data = Client.objects.get(slug_name=slug_name).doublegis_set.all()
        elif resurs == 'otzovik':
            data = Client.objects.get(slug_name=slug_name).otzovik_set.all()
        return reversed(data)

    @staticmethod
    def get_data_for_date(kwargs):
        slug_name = kwargs.get('slug_name')
        resurs = kwargs.get('resurs')
        date = kwargs.get('date')
        date = datetime.strptime(date, '%d.%m.%Y')

        if resurs == 'yandex':
            data = Client.objects.get(slug_name=slug_name).yandex_set.filter(create_at=date)
        elif resurs == 'google':
            data = Client.objects.get(slug_name=slug_name).googlemaps_set.get(create_at=date)
        elif resurs == 'double_gis':
            data = Client.objects.get(slug_name=slug_name).doublegis_set.get(create_at=date)
        elif resurs == 'otzovik':
            data = Client.objects.get(slug_name=slug_name).otzovik_set.filter(create_at=date).values('raiting', 'count_comments', 'create_at', 'recommend')
        print(data)
        return list(data)





