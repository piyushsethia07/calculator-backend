import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000/api'
    
    def test_user_api(self):
        # Test creating a new user
        create_user_url = f"{self.base_url}/users"
        user_data = {'mobile_number': '1234567890', 'email': 'test@example.com', 'name': 'Test User'}
        response = requests.post(create_user_url, json=user_data)
        self.assertEqual(response.status_code, 201)

        # Test getting all users
        get_users_url = f"{self.base_url}/users"
        response = requests.get(get_users_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Test updating an existing user
        updated_user_data = {'email': 'updated@example.com'}
        update_user_url = f"{self.base_url}/users/1"
        response = requests.put(update_user_url, json=updated_user_data)
        self.assertEqual(response.status_code, 200)

        # Test deleting an existing user
        delete_user_url = f"{self.base_url}/users/1"
        response = requests.delete(delete_user_url)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
