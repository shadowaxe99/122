import unittest
from backend_system.ai_agent_platform.brand_database import BrandDatabase

class TestBrandDatabase(unittest.TestCase):

    def setUp(self):
        self.brand_database = BrandDatabase()

    def test_add_brand(self):
        brand_data = {
            'name': 'Brand X',
            'industry': 'Fashion',
            'preferences': ['Fashion', 'Lifestyle']
        }
        self.brand_database.add_brand(brand_data)
        self.assertIn('Brand X', self.brand_database.brands)

    def test_remove_brand(self):
        brand_data = {
            'name': 'Brand Y',
            'industry': 'Tech',
            'preferences': ['Tech', 'Gaming']
        }
        self.brand_database.add_brand(brand_data)
        self.brand_database.remove_brand('Brand Y')
        self.assertNotIn('Brand Y', self.brand_database.brands)

    def test_update_brand(self):
        brand_data = {
            'name': 'Brand Z',
            'industry': 'Food',
            'preferences': ['Food', 'Cooking']
        }
        updated_data = {
            'name': 'Brand Z',
            'industry': 'Food',
            'preferences': ['Food', 'Cooking', 'Health']
        }
        self.brand_database.add_brand(brand_data)
        self.brand_database.update_brand('Brand Z', updated_data)
        self.assertEqual(self.brand_database.brands['Brand Z']['preferences'], ['Food', 'Cooking', 'Health'])

    def test_get_brand(self):
        brand_data = {
            'name': 'Brand A',
            'industry': 'Travel',
            'preferences': ['Travel', 'Adventure']
        }
        self.brand_database.add_brand(brand_data)
        retrieved_brand = self.brand_database.get_brand('Brand A')
        self.assertEqual(retrieved_brand, brand_data)

if __name__ == '__main__':
    unittest.main()