from cars.models import CarBrand
from cars.serializers import CarBrandSerializer
from cars.tests.excepted_data import test_data
from rest_framework import status
from rest_framework.test import APITestCase


class BrandsApiTestCase(APITestCase):
    url_api = '/api/v1/brands'

    def create_car_brands(self):
        car_brand_1 = CarBrand.objects.create(name='BWM')
        car_brand_2 = CarBrand.objects.create(name='LADA')
        car_brand_3 = CarBrand.objects.create(name='Toyota')
        car_brand_4 = CarBrand.objects.create(name='Geely')
        car_brand_5 = CarBrand.objects.create(name='Opel')
        car_brands = (
            car_brand_1,
            car_brand_2,
            car_brand_3,
            car_brand_4,
            car_brand_5
        )
        return car_brands

    def test_create(self):
        url = self.url_api + '/create/'
        data = test_data["brands"]["data"]
        for brand in data:
            r = self.client.post(
                url,
                data=brand,
                format='json'
            )
            self.assertEqual(status.HTTP_201_CREATED, r.status_code)
        r = self.client.post(url, data={'name': ''}, format='json')
        expected_data = test_data["brands"]["bad"]["blank"]
        self.assertEqual(status.HTTP_400_BAD_REQUEST, r.status_code)
        self.assertEqual(expected_data, r.data)
        r = self.client.post(url, data={'name': 'BMW'}, format='json')
        expected_data = test_data["brands"]["bad"]["already"]
        self.assertEqual(status.HTTP_400_BAD_REQUEST, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_all(self):
        url = self.url_api + '/all/'
        brands_created = self.create_car_brands()
        brands_count = CarBrand.objects.all().count()
        r = self.client.get(url, format='json')
        serializer_data = CarBrandSerializer(brands_created, many=True).data
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(brands_count, len(r.data))
        self.assertEqual(serializer_data, r.data)

    def test_get_detail(self):
        brand_created = self.create_car_brands()[0]
        id_brand = str(brand_created.id)
        url = self.url_api + '/detail/' + id_brand
        r = self.client.get(url, format='json')
        car_brand = CarBrand.objects.get(id=id_brand)
        serializer_data = CarBrandSerializer(brand_created).data
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(serializer_data, r.data)
        self.assertEqual(car_brand.name, r.data['name'])
        self.assertEqual(len(CarBrand._meta.fields), len(r.data))

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["brands"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_patch_detail(self):
        brand_created = self.create_car_brands()[0]
        id_brand = str(brand_created.id)
        url = self.url_api + '/detail/' + id_brand
        data = {"name": "Mitsubishi"}
        r = self.client.patch(url, format='json', data=data)
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual("Mitsubishi", r.data['name'])
        self.assertEqual(len(CarBrand._meta.fields), len(r.data))

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["brands"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_delete_detail(self):
        brand_created = self.create_car_brands()[0]
        id_brand = str(brand_created.id)
        url = self.url_api + '/detail/' + id_brand
        r = self.client.delete(url, format='json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, r.status_code)

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["brands"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)
