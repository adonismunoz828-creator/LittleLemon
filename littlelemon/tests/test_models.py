from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream",
            price=80,
            inventory=100
        )
        self.assertEqual(str(item), "IceCream")

    def test_string_representation(self):
        menu = Menu.objects.create(
            title="Pizza",
            price=250.00,
            inventory=10
        )

        self.assertEqual(str(menu), "Pizza")