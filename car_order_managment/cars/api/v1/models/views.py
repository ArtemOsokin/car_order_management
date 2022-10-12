import django_filters.rest_framework
from rest_framework import generics
from cars.serializers import CarModelSerializer
from cars.models import CarModel


class CarModelCreateView(generics.CreateAPIView):
    serializer_class = CarModelSerializer


class CarModelListView(generics.ListAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()


class CarModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()
