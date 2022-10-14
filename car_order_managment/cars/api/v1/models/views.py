from cars.models import CarModel
from cars.serializers import CarModelSerializer
from rest_framework import generics


class CarModelCreateView(generics.CreateAPIView):
    serializer_class = CarModelSerializer


class CarModelListView(generics.ListAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()


class CarModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()
