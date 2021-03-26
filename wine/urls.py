from django.urls import path
from wine.views import WineDetail, WineList, EvaluationList

app_name = 'wine'

urlpatterns = [
    path('', WineList.as_view(), name='wine_list'),
    path('detail/<int:pk>/', WineDetail.as_view(), name='wine_detail'),
    path('evaluations', EvaluationList.as_view(), name='evaluation_list'),
]