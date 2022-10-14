import random

from cars.models import CarModel, CarBrand
from cars.serializers import CarModelSerializer
from cars.tests.excepted_data import test_data
from rest_framework import status
from rest_framework.test import APITestCase


class ModlesApiTestCase(APITestCase):
    url_api = '/api/v1/models'

    def create_car_models(self):
        car_brand_1 = CarBrand.objects.create(name='BWM')
        car_brand_2 = CarBrand.objects.create(name='LADA')
        car_model_1 = CarModel.objects.create(
            name='M5',
            car_brand=car_brand_1
        )
        car_model_2 = CarModel.objects.create(
            name='X6',
            car_brand=car_brand_1
        )
        car_model_3 = CarModel.objects.create(
            name='2110',
            car_brand=car_brand_2
        )
        car_model_4 = CarModel.objects.create(
            name='Vesta',
            car_brand=car_brand_2
        )
        car_model_5 = CarModel.objects.create(
            name='X-Ray',
            car_brand=car_brand_2
        )
        car_models = (
            car_model_1,
            car_model_2,
            car_model_3,
            car_model_4,
            car_model_5
        )
        return car_models

    def test_create(self):
        url = self.url_api + '/create/'
        data = test_data["models"]["data"]
        car_brands = (
            CarBrand.objects.create(name='BWM'),
            CarBrand.objects.create(name='LADA')
        )
        for model in data:
            car_brand = random.choice(car_brands)
            model['car_brand'] = str(car_brand.id)
            r = self.client.post(
                url,
                data=model,
                format='json'
            )
            self.assertEqual(status.HTTP_201_CREATED, r.status_code)
        r = self.client.post(url, data={'name': ''}, format='json')
        expected_data = test_data["models"]["bad"]["required"]
        self.assertEqual(status.HTTP_400_BAD_REQUEST, r.status_code)
        self.assertEqual(expected_data, r.data)
        r = self.client.post(
            url,
            data={'name': 'M5', 'car_brand': CarBrand.objects.first().id},
            format='json'
        )
        expected_data = test_data["models"]["bad"]["already"]
        self.assertEqual(status.HTTP_400_BAD_REQUEST, r.status_code)
        self.assertEqual(expected_data, r.data)
        r = self.client.post(
            url,
            data={'name': '', 'car_brand': CarBrand.objects.first().id},
            format='json'
        )
        expected_data = test_data["models"]["bad"]["blank"]
        self.assertEqual(status.HTTP_400_BAD_REQUEST, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_all(self):
        url = self.url_api + '/all/'
        models = self.create_car_models()
        models_count = CarModel.objects.all().count()
        r = self.client.get(url, format='json')
        serializer_data = CarModelSerializer(models, many=True).data
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(models_count, len(r.data))
        self.assertEqual(serializer_data, r.data)

    def test_get_detail(self):
        model = self.create_car_models()[0]
        id_model = str(model.id)
        url = self.url_api + '/detail/' + id_model
        r = self.client.get(url, format='json')
        car_model = CarModel.objects.get(id=id_model)
        serializer_data = CarModelSerializer(model).data
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(serializer_data, r.data)
        self.assertEqual(car_model.name, r.data['name'])
        self.assertEqual(car_model.car_brand.id, r.data['car_brand'])
        self.assertEqual(len(CarModel._meta.fields), len(r.data))

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["models"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_patch_detail(self):
        models = self.create_car_models()[0]
        id_model = str(models.id)
        url = self.url_api + '/detail/' + id_model
        data = {"name": "Camry"}
        r = self.client.patch(url, format='json', data=data)
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual("Camry", r.data['name'])
        self.assertEqual(len(CarModel._meta.fields), len(r.data))

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["models"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_delete_detail(self):
        model = self.create_car_models()[0]
        id_model = str(model.id)
        url = self.url_api + '/detail/' + id_model
        r = self.client.delete(url, format='json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, r.status_code)

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["models"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)
