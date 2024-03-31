from models import User, Category, Product, Transaction, TransactionBreakdown

# User Endpoints
def get_users(session):
    users = User.query.all()
    return [{'id': user.id, 'mobile_number': user.mobile_number, 'email': user.email, 'name': user.name} for user in users]

def create_user(data, session):
    user = User(mobile_number=data['mobile_number'], email=data['email'] if 'email' in data else None, name=data['name'] if 'name' in data else None)
    session.add(user)
    session.commit()
    return {'message': 'User created successfully'}, 201

def update_user(user_id, data, session):
    user = User.query.get(user_id)
    if not user:
        raise Exception('User not found')
    user.mobile_number = data.get('mobile_number', user.mobile_number)
    user.email = data.get('email', user.email)
    user.name = data.get('name', user.name)
    session.commit()
    return {'message': 'User updated successfully'}

def delete_user(user_id, session):
    user = User.query.get(user_id)
    if not user:
        raise Exception('User not found')
    session.delete(user)
    session.commit()
    return {'message': 'User deleted successfully'}

# Category Endpoints
def get_categories(session):
    categories = Category.query.all()
    return [{'id': category.id, 'name': category.name} for category in categories]

def create_category(data, session):
    category = Category(name=data['name'])
    session.add(category)
    session.commit()
    return {'message': 'Category created successfully'}, 201

def update_category(category_id, data, session):
    category = Category.query.get(category_id)
    if not category:
        raise Exception('Category not found')
    category.name = data.get('name', category.name)
    session.commit()
    return {'message': 'Category updated successfully'}

def delete_category(category_id, session):
    category = Category.query.get(category_id)
    if not category:
        raise Exception('Category not found')
    session.delete(category)
    session.commit()
    return {'message': 'Category deleted successfully'}

# Product Endpoints
def get_products(session):
    products = Product.query.all()
    return [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'category_id': product.category_id} for product in products]

def create_product(data, session):
    product = Product(name=data['name'], description=data['description'], price=data['price'], category_id=data['category_id'])
    session.add(product)
    session.commit()
    return {'message': 'Product created successfully'}, 201

def update_product(product_id, data, session):
    product = Product.query.get(product_id)
    if not product:
        raise Exception('Product not found')
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.category_id = data.get('category_id', product.category_id)
    session.commit()
    return {'message': 'Product updated successfully'}

def delete_product(product_id, session):
    product = Product.query.get(product_id)
    if not product:
        raise Exception('Product not found')
    session.delete(product)
    session.commit()
    return {'message': 'Product deleted successfully'}

# Transaction Endpoints
def get_transactions(session):
    transactions = Transaction.query.all()
    return [{'id': transaction.id, 'mobile_number': transaction.mobile_number, 'transaction_amount': transaction.transaction_amount, 'transaction_type': transaction.transaction_type, 'cash_in_out': transaction.cash_in_out, 'person_name': transaction.person_name, 'created_at': transaction.created_at} for transaction in transactions]

def create_transaction(data, session):
    transaction = Transaction(mobile_number=data['mobile_number'], transaction_amount=data['transaction_amount'], transaction_type=data['transaction_type'], cash_in_out=data['cash_in_out'], person_name=data['person_name'] if 'person_name' in data else None)
    session.add(transaction)
    session.commit()
    return {'message': 'Transaction created successfully'}, 201

def update_transaction(transaction_id, data, session):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        raise Exception('Transaction not found')
    transaction.mobile_number = data.get('mobile_number', transaction.mobile_number)
    transaction.transaction_amount = data.get('transaction_amount', transaction.transaction_amount)
    transaction.transaction_type = data.get('transaction_type', transaction.transaction_type)
    transaction.cash_in_out = data.get('cash_in_out', transaction.cash_in_out)
    transaction.person_name = data.get('person_name', transaction.person_name)
    session.commit()
    return {'message': 'Transaction updated successfully'}

def delete_transaction(transaction_id, session):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        raise Exception('Transaction not found')
    session.delete(transaction)
    session.commit()
    return {'message': 'Transaction deleted successfully'}

# Transaction Breakdown Endpoints
def get_transaction_breakdowns(session):
    transaction_breakdowns = TransactionBreakdown.query.all()
    return [{'id': breakdown.id, 'transaction_id': breakdown.transaction_id, 'product_id': breakdown.product_id, 'quantity': breakdown.quantity} for breakdown in transaction_breakdowns]

def create_transaction_breakdown(data, session):
    breakdown = TransactionBreakdown(transaction_id=data['transaction_id'], product_id=data['product_id'], quantity=data['quantity'])
    session.add(breakdown)
    session.commit()
    return {'message': 'Transaction breakdown created successfully'}, 201

def update_transaction_breakdown(breakdown_id, data, session):
    breakdown = TransactionBreakdown.query.get(breakdown_id)
    if not breakdown:
        raise Exception('Transaction breakdown not found')
    breakdown.transaction_id = data.get('transaction_id', breakdown.transaction_id)

def delete_transaction_breakdown(breakdown_id, data, session):
    breakdown = TransactionBreakdown.query.get(breakdown_id)
    if not breakdown:
        raise Exception('Transaction breakdown not found')
    session.delete(breakdown)
    session.commit()
    return {'message': 'Transaction breakdown deleted successfully'}
   
