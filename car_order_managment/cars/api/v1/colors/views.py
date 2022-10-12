from rest_framework import generics
from cars.serializers import ColorSerializer
from cars.models import Color


class ColorCreateView(generics.CreateAPIView):
    serializer_class = ColorSerializer


class ColorListView(generics.ListAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


class ColorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
