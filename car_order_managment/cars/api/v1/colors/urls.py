from cars.api.v1.colors.views import *
from django.urls import path

app_name = 'colors'
urlpatterns = [
    path('create/', ColorCreateView.as_view()),
    path('all/', ColorListView.as_view()),
    path('detail/<uuid:pk>', ColorDetailView.as_view()),
    path('sum/', ColorSumView.as_view())
]
