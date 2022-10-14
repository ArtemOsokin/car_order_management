from cars.models import Color
from cars.serializers import ColorSerializer, ColorSumSerializer
from django.db.models import Sum
from rest_framework import generics


class ColorCreateView(generics.CreateAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


class ColorListView(generics.ListAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


class ColorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


class ColorSumView(generics.ListAPIView):
    serializer_class = ColorSumSerializer
    queryset = Color.objects.all().annotate(
        color_amount=Sum('orders__amount')
    )
