from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemsViews(TestCase):

    def setUp(self):
        salad = MenuItem.objects.create(title='Salad', price=5.00, inventory=20)
        pizza = MenuItem.objects.create(title='Pizza', price=6.00, inventory=20)
    
    def test_menu_item(self):
        salad = MenuItem.objects.get(title='Salad')
        pizza = MenuItem.objects.get(title='Pizza')

        self.assertEqual(str(salad), 'Salad : 5.00')
        self.assertEqual(str(pizza), 'Pizza : 6.00')
    