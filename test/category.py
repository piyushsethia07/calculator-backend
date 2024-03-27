import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000/api'
    
    def test_category_api(self):
        # Test creating a new category
        create_category_url = f"{self.base_url}/categories"
        category_data = {'name': 'Test Category'}
        response = requests.post(create_category_url, json=category_data)
        self.assertEqual(response.status_code, 201)

        # Test getting all categories
        get_categories_url = f"{self.base_url}/categories"
        response = requests.get(get_categories_url)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Test updating an existing category
        updated_category_data = {'name': 'Updated Category'}
        update_category_url = f"{self.base_url}/categories/1"
        response = requests.put(update_category_url, json=updated_category_data)
        self.assertEqual(response.status_code, 200)

        # Test deleting an existing category
        delete_category_url = f"{self.base_url}/categories/1"
        response = requests.delete(delete_category_url)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
