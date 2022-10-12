from cars.models import Color, CarModel, CarBrand, Order
from rest_framework import serializers


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    car_brand = serializers.SerializerMethodField()

    def get_car_brand(self, obj):
        return obj.car_model.car_brand.id

    class Meta:
        model = Order
        fields = [
            'data_order',
            'color',
            'car_model',
            'car_brand',
            'amount'
        ]