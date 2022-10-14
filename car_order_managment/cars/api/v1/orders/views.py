from cars.models import Order
from cars.serializers import OrderDetailSerializer, OrderListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import pagination
from rest_framework.filters import OrderingFilter


class PaginationOrder(pagination.LimitOffsetPagination):
    default_limit = 10


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()
    pagination_class = PaginationOrder
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['car_model']
    ordering_fields = ['amount']


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
