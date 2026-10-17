from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=250, inventory=10)
        Menu.objects.create(title="Pasta", price=180, inventory=5)

    def test_getall(self):
        client = APIClient()
        response = client.get('/restaurant/menu/items')

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)