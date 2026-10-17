from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_string_representation(self):
        menu = Menu.objects.create(
            title="Pizza",
            price=250.00,
            inventory=10
        )

        self.assertEqual(str(menu), "Pizza")