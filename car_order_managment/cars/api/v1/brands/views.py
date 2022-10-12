from rest_framework import generics
from cars.serializers import CarBrandSerializer
from cars.models import CarBrand


class CarBrandCreateView(generics.CreateAPIView):
    serializer_class = CarBrandSerializer


class CarBrandListView(generics.ListAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.all()


class CarBrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.all()
