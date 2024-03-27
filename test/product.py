import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000/api'
    
    def test_product_api(self):
        # Test creating a new product
        create_product_url = f"{self.base_url}/products"
        product_data = {'name': 'Test Product', 'description': 'Test Description', 'price': 10.99, 'category_id': 10}
        response = requests.post(create_product_url, json=product_data)
        self.assertEqual(response.status_code, 201)

        # Test getting all products
        get_products_url = f"{self.base_url}/products"
        response = requests.get(get_products_url)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Test updating an existing product
        updated_product_data = {'name': 'Updated Product', 'price': 15.99}
        update_product_url = f"{self.base_url}/products/1"
        response = requests.put(update_product_url, json=updated_product_data)
        self.assertEqual(response.status_code, 200)

        # Test deleting an existing product
        delete_product_url = f"{self.base_url}/products/1"
        response = requests.delete(delete_product_url)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
