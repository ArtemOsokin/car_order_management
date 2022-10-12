from django.urls import path
from cars.api.v1.models.views import *


app_name = 'models'
urlpatterns = [
    path('create/', CarModelCreateView.as_view()),
    path('all/', CarModelListView.as_view()),
    path('detail/<uuid:pk>', CarModelDetailView.as_view())
]
