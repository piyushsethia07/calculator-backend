import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000/api'
    
    def test_transaction_breakdown_api(self):
        # Test creating a new transaction breakdown
        create_breakdown_url = f"{self.base_url}/transaction-breakdowns"
        breakdown_data = {'transaction_id': 1, 'product_id': 1, 'quantity': 2}
        response = requests.post(create_breakdown_url, json=breakdown_data)
        self.assertEqual(response.status_code, 201)

        # Test getting all transaction breakdowns
        get_breakdowns_url = f"{self.base_url}/transaction-breakdowns"
        response = requests.get(get_breakdowns_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Test updating an existing transaction breakdown
        updated_breakdown_data = {'quantity': 3}
        update_breakdown_url = f"{self.base_url}/transaction-breakdowns/1"
        response = requests.put(update_breakdown_url, json=updated_breakdown_data)
        self.assertEqual(response.status_code, 200)

        # Test deleting an existing transaction breakdown
        delete_breakdown_url = f"{self.base_url}/transaction-breakdowns/1"
        response = requests.delete(delete_breakdown_url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
