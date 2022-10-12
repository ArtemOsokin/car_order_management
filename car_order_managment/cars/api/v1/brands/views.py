from rest_framework import generics
from cars.serializers import CarBrandSerializer, CarBrandSumSerializer
from cars.models import CarBrand
from django.db.models import Sum


class CarBrandCreateView(generics.CreateAPIView):
    serializer_class = CarBrandSerializer


class CarBrandListView(generics.ListAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.all()


class CarBrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.all()


class CarBrandSumView(generics.ListAPIView):
    serializer_class = CarBrandSumSerializer
    queryset = CarBrand.objects.all().annotate(
        car_brand_amount=Sum('car_models__orders__amount')
    )