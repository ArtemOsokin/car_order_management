import datetime
import random

from cars.models import CarModel, CarBrand, Color, Order
from cars.serializers import OrderListSerializer, OrderDetailSerializer
from cars.tests.excepted_data import test_data
from rest_framework import status
from rest_framework.test import APITestCase


class OrdersApiTestCase(APITestCase):
    url_api = '/api/v1/orders'

    def create_orders(self):
        car_brand_BWM = CarBrand.objects.create(name='BWM')
        car_brand_LADA = CarBrand.objects.create(name='LADA')
        car_model_M5 = CarModel.objects.create(
            name='M5',
            car_brand=car_brand_BWM
        )
        car_model_Vesta = CarModel.objects.create(
            name='Vesta',
            car_brand=car_brand_LADA
        )
        color_green = Color.objects.create(name='Green')
        color_red = Color.objects.create(name='Red')
        orders = (
            Order.objects.create(
                color=color_green,
                car_model=car_model_M5,
                amount=15,
                data_order=datetime.datetime.now()
            ),
            Order.objects.create(
                color=color_red,
                car_model=car_model_Vesta,
                amount=10,
                data_order=datetime.datetime.now()
            ),
            Order.objects.create(
                color=color_green,
                car_model=car_model_Vesta,
                amount=17,
                data_order=datetime.datetime.now()
            )
        )
        return orders

    def test_create(self):
        url = self.url_api + '/create/'
        car_brands = (
            CarBrand.objects.create(name='BWM'),
            CarBrand.objects.create(name='LADA')
        )
        car_models = (
            CarModel.objects.create(
                name='X5',
                car_brand=random.choice(car_brands)
            ),
            CarModel.objects.create(
                name='Vesta',
                car_brand=random.choice(car_brands)
            ),
        )
        colors = (
            Color.objects.create(name='Green'),
            Color.objects.create(name='Red'),
            Color.objects.create(name='Black')
        )

        for _ in range(10):
            data = {
                'car_model': str(random.choice(car_models).id),
                'color': str(random.choice(colors).id),
                'amount': random.randint(1, 35),
                'data_order': datetime.datetime.now()
            }

            r = self.client.post(
                url,
                data=data,
                format='json'
            )
            self.assertEqual(status.HTTP_201_CREATED, r.status_code)
        data = {
            'car_model': "",
            'color': "",
            'amount': "",
            'data_order': datetime.datetime.now()
        }
        r = self.client.post(
            url,
            data=data,
            format='json'
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, r.status_code)

    def test_all(self):
        url = self.url_api + '/all/'
        orders_created = self.create_orders()
        orders_count = Order.objects.all().count()
        r = self.client.get(url, format='json')
        serializer_data = OrderListSerializer(orders_created, many=True).data
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(orders_count, len(r.data["results"]))
        self.assertEqual(serializer_data, r.data["results"])

    def test_get_detail(self):
        created_order = self.create_orders()[0]
        id_order = str(created_order.id)
        url = self.url_api + '/detail/' + id_order
        r = self.client.get(url, format='json')
        order = Order.objects.get(id=id_order)
        serializer_data = OrderDetailSerializer(order).data
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(serializer_data, r.data)
        self.assertEqual(order.car_model.id, r.data['car_model'])
        self.assertEqual(order.color.id, r.data['color'])
        self.assertEqual(order.amount, r.data['amount'])
        self.assertEqual(len(Order._meta.fields), len(r.data))

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["orders"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_patch_detail(self):
        orders = self.create_orders()[0]
        id_order = str(orders.id)
        url = self.url_api + '/detail/' + id_order
        data = {"amount": 322}
        r = self.client.patch(url, format='json', data=data)
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(322, r.data['amount'])
        self.assertEqual(len(Order._meta.fields), len(r.data))

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["orders"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_delete_detail(self):
        orders = self.create_orders()[0]
        id_order = str(orders.id)
        url = self.url_api + '/detail/' + id_order
        r = self.client.delete(url, format='json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, r.status_code)

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["orders"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)
