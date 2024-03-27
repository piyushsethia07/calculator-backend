from db_config import db
import time

class BaseModel(db.Model):
    __abstract__ = True
    created_at = db.Column(db.BigInteger, default=int(time.time() * 1000))
    updated_at = db.Column(db.BigInteger, default=int(time.time() * 1000), onupdate=int(time.time() * 1000))
    created_by = db.Column(db.String, nullable=False, default='Kashi')
    updated_by = db.Column(db.String, nullable=False, default='Kashi')

# Models
class User(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    name = db.Column(db.String(120), nullable=True)
    verified = db.Column(db.Boolean, nullable=False, default=False)

class Category(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Product(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

class Transaction(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(20), nullable=False)
    transaction_amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)
    cash_in_out = db.Column(db.String(20), nullable=False)
    person_name = db.Column(db.String(120), nullable=True)

class TransactionBreakdown(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transaction.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref=db.backref('transaction_breakdowns', lazy=True))
    transaction = db.relationship('Transaction', backref=db.backref('transaction_breakdowns', lazy=True))