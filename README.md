# calculator-backend

base_url = https://calculator-service-pk-embedded-solution.koyeb.app

### Health endpoint
Endpoint: GET /health

### Create Transaction
Endpoint: POST /api/transactions
Input:
```json
{
    "mobile_number": "1234567890",
    "transaction_amount": 50.0,
    "transaction_type": "Credit",
    "cash_in_out": "In",
    "person_name": "Test Person"
}