from cars.models import Order
from cars.serializers import OrderDetailSerializer, OrderListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import pagination


class PaginationOrder(pagination.LimitOffsetPagination):
    default_limit = 10


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all().order_by('-amount')
    pagination_class = PaginationOrder
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['car_model']


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
