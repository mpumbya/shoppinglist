import unittest
from shoplist import ShopList

class shop_List(unittest.TestCase):
    def setUp(self):
        self.amazon_list = ShopList()

    def test_create_items(self):
        self.amazon_list.add_item('coco')
        self.assertEqual(self.amazon_list.items, ['coco'], msg= 'items not added')

    def test_remove_items(self):
        self.amazon_list.items.append('cat')
        self.amazon_list.items.append('goat') 
        self.amazon_list.remove_item('cat')
        self.assertEqual(self.amazon_list.items, ['goat'], msg='items not removed')
        
        