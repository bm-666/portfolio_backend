
from django.urls import path
from api.views.views import APIData
from api.views.ClientsViews import AllClients, ClientDetail
from api.views.DataViews import AllDataResurs, DataForDate

urlpatterns = [
    path('v2/data', APIData.as_view()),
    path('v2/clients', AllClients.as_view()),
    path('v2/clients/<str:slug_name>', ClientDetail.as_view()),
    path('v2/clients/<str:slug_name>/<str:resurs>/', AllDataResurs.as_view()),
    path('v2/clients/<str:slug_name>/<str:resurs>/<str:date>', DataForDate.as_view())
    #path('v2/clients/<str:slug_name>/<str:resurs>/<str:date_parse>')

]
