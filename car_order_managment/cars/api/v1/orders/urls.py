from django.urls import path, include
from cars.api.v1.orders.views import *


app_name = 'orders'
urlpatterns = [
    path('create/', OrderCreateView.as_view()),
    path('all/', OrderListView.as_view()),
    path('detail/<uuid:pk>', OrderDetailView.as_view())
]
