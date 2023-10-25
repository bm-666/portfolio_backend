from rest_framework.views import APIView
from rest_framework.response import SimpleTemplateResponse, Response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from api.models import Client
from api.forms import RaitingDateForm
from .UtilsViews import DataClientModels


class AllDataResurs(APIView):
    template: str = 'raiting.html'
    context: dict = {}
    @method_decorator(login_required)
    def get(self, request,  slug_name, resurs):
        form = RaitingDateForm()
        data = DataClientModels().get_all_data_resurs(resurs, slug_name)
        self.context.update()
        self.context.update({
            'raiting':list(data),
            'form': form
        })
        return SimpleTemplateResponse(template=self.template, context=self.context)

class DataForDate(APIView):

    def get(self, request, **kwargs):
        data: list = DataClientModels().get_data_for_date(kwargs)
        if data:
            date_statistic: dict = {
                'raiting': data[0].get('raiting'),
                'count_comments': data[0].get('count_comments'),
                'create_at': data[0].get('create_at'),
                'recommend': data[0].get('recommend')
            }
        else:
            date_statistic: dict = {'raiting': 'None', 'count_comments': 'None', 'create_at': 'None', 'recommend': 'None'}
        return Response(date_statistic)

