import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000/api'
    
    def test_transaction_api(self):
        # Test creating a new transaction
        create_transaction_url = f"{self.base_url}/transactions"
        transaction_data = {'mobile_number': '1234567890', 'transaction_amount': 50.0, 'transaction_type': 'Credit', 'cash_in_out': 'In', 'person_name': 'Test Person'}
        response = requests.post(create_transaction_url, json=transaction_data)
        self.assertEqual(response.status_code, 201)

        # Test getting all transactions
        get_transactions_url = f"{self.base_url}/transactions"
        response = requests.get(get_transactions_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Test updating an existing transaction
        updated_transaction_data = {'transaction_amount': 75.0}
        update_transaction_url = f"{self.base_url}/transactions/1"
        response = requests.put(update_transaction_url, json=updated_transaction_data)
        self.assertEqual(response.status_code, 200)

        # Test deleting an existing transaction
        delete_transaction_url = f"{self.base_url}/transactions/1"
        response = requests.delete(delete_transaction_url)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
