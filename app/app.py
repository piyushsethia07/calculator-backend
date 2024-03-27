from flask import Flask, request, jsonify
from crud import *
from db_config import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/health', methods=['GET'])
def health_api():
    return {"message": "Success"}

# User Endpoints
@app.route('/api/users', methods=['GET'])
def get_all_users():
    users = get_users(db.session)
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_new_user():
    data = request.json
    response, status_code = create_user(data, db.session)
    return jsonify(response), status_code

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_existing_user(user_id):
    data = request.json
    try:
        response = update_user(user_id, data, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_existing_user(user_id):
    try:
        response = delete_user(user_id, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

# Category Endpoints
@app.route('/api/categories', methods=['GET'])
def get_all_categories():
    categories = get_categories(db.session)
    return jsonify(categories)

@app.route('/api/categories', methods=['POST'])
def create_new_category():
    data = request.json
    response, status_code = create_category(data, db.session)
    return jsonify(response), status_code

@app.route('/api/categories/<int:category_id>', methods=['PUT'])
def update_existing_category(category_id):
    data = request.json
    try:
        response = update_category(category_id, data, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

@app.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_existing_category(category_id):
    try:
        response = delete_category(category_id, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

# Product Endpoints
@app.route('/api/products', methods=['GET'])
def get_all_products():
    products = get_products(db.session)
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def create_new_product():
    data = request.json
    response, status_code = create_product(data, db.session)
    return jsonify(response), status_code

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_existing_product(product_id):
    data = request.json
    try:
        response = update_product(product_id, data, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_existing_product(product_id):
    try:
        response = delete_product(product_id, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

# Transaction Endpoints
@app.route('/api/transactions', methods=['GET'])
def get_all_transactions():
    transactions = get_transactions(db.session)
    return jsonify(transactions)

@app.route('/api/transactions', methods=['POST'])
def create_new_transaction():
    data = request.json
    response, status_code = create_transaction(data, db.session)
    return jsonify(response), status_code

@app.route('/api/transactions/<int:transaction_id>', methods=['PUT'])
def update_existing_transaction(transaction_id):
    data = request.json
    try:
        response = update_transaction(transaction_id, data, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

@app.route('/api/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_existing_transaction(transaction_id):
    try:
        response = delete_transaction(transaction_id, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

# Transaction Breakdown Endpoints
@app.route('/api/transaction-breakdowns', methods=['GET'])
def get_all_transaction_breakdowns():
    transaction_breakdowns = get_transaction_breakdowns(db.session)
    return jsonify(transaction_breakdowns)

@app.route('/api/transaction-breakdowns', methods=['POST'])
def create_new_transaction_breakdown():
    data = request.json
    response, status_code = create_transaction_breakdown(data, db.session)
    return jsonify(response), status_code

@app.route('/api/transaction-breakdowns/<int:breakdown_id>', methods=['PUT'])
def update_existing_transaction_breakdown(breakdown_id):
    data = request.json
    try:
        response = update_transaction_breakdown(breakdown_id, data, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

@app.route('/api/transaction-breakdowns/<int:breakdown_id>', methods=['DELETE'])
def delete_existing_transaction_breakdown(breakdown_id):
    try:
        response = delete_transaction_breakdown(breakdown_id, db.session)
        return jsonify(response)
    except Exception as e:
        return str(e), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
