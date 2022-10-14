from cars.api.v1.models.views import *
from django.urls import path

app_name = 'models'
urlpatterns = [
    path('create/', CarModelCreateView.as_view()),
    path('all/', CarModelListView.as_view()),
    path('detail/<uuid:pk>', CarModelDetailView.as_view())
]
