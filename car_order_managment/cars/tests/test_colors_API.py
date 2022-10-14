from cars.models import Color
from cars.serializers import ColorSerializer
from cars.tests.excepted_data import test_data
from rest_framework import status
from rest_framework.test import APITestCase


class ColorsApiTestCase(APITestCase):
    url_api = '/api/v1/colors'

    def create_colors(self):
        color_green = Color.objects.create(name='Green')
        color_red = Color.objects.create(name='Red')
        color_black = Color.objects.create(name='Black')
        color_white = Color.objects.create(name='White')
        color_yellow = Color.objects.create(name='Yellow')
        colors = (
            color_green,
            color_red,
            color_black,
            color_white,
            color_yellow
        )
        return colors

    def test_create(self):
        url = self.url_api + '/create/'
        data = test_data["colors"]["data"]
        for color in data:
            r = self.client.post(
                url,
                data=color,
                format='json'
            )
            self.assertEqual(status.HTTP_201_CREATED, r.status_code)
        r = self.client.post(url, data={'name': ''}, format='json')
        expected_data = test_data["colors"]["bad"]["blank"]
        self.assertEqual(status.HTTP_400_BAD_REQUEST, r.status_code)
        self.assertEqual(expected_data, r.data)
        r = self.client.post(url, data={'name': 'Red'}, format='json')
        expected_data = test_data["colors"]["bad"]["already"]
        self.assertEqual(status.HTTP_400_BAD_REQUEST, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_all(self):
        url = self.url_api + '/all/'
        colors_created = self.create_colors()
        colors_count = Color.objects.all().count()
        r = self.client.get(url, format='json')
        serializer_data = ColorSerializer(colors_created, many=True).data
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(colors_count, len(r.data))
        self.assertEqual(serializer_data, r.data)

    def test_get_detail(self):
        color_created = self.create_colors()[0]
        id_color = str(color_created.id)
        url = self.url_api + '/detail/' + id_color
        r = self.client.get(url, format='json')
        color = Color.objects.get(id=id_color)
        serializer_data = ColorSerializer(color_created).data
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual(serializer_data, r.data)
        self.assertEqual(color.name, r.data['name'])
        self.assertEqual(len(Color._meta.fields), len(r.data))

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["colors"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_patch_detail(self):
        color_created = self.create_colors()[0]
        id_color = str(color_created.id)
        url = self.url_api + '/detail/' + id_color
        data = {"name": "Purple"}
        r = self.client.patch(url, format='json', data=data)
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual("Purple", r.data['name'])
        self.assertEqual(len(Color._meta.fields), len(r.data))

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["colors"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)

    def test_delete_detail(self):
        color_created = self.create_colors()[0]
        id_color = str(color_created.id)
        url = self.url_api + '/detail/' + id_color
        r = self.client.delete(url, format='json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, r.status_code)

        url = self.url_api + '/detail/68daa1f6-47e6-419b-a3df-3f754af8411c'
        expected_data = test_data["colors"]["bad"]['404']
        r = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, r.status_code)
        self.assertEqual(expected_data, r.data)
