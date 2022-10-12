from django.urls import path
from cars.api.v1.brands.views import *


app_name = 'brands'
urlpatterns = [
    path('create/', CarBrandCreateView.as_view()),
    path('all/', CarBrandListView.as_view()),
    path('detail/<uuid:pk>', CarBrandDetailView.as_view()),
    path('sum/', CarBrandSumView.as_view()),
]
