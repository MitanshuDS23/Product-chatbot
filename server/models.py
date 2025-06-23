# models.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = "products"
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(128), nullable=False)
    category    = db.Column(db.String(64), nullable=False)
    price       = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

def init_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    with app.app_context():
        db.create_all()

def reset_and_seed():
    """Delete everything in products and add 100 new mock items."""
    # This function must be called inside an app_context
    Product.query.delete()
    for i in range(1, 101):
        p = Product(
            name=f"Product {i}",
            category="electronics" if i % 2 == 0 else "books",
            price=round(100 + i * 2.5, 2),
            description=f"Sample description for Product {i}"
        )
        db.session.add(p)
    db.session.commit()

def search_products(query: str):
    pattern = f"%{query}%"
    results = (
        Product.query
               .filter(Product.name.ilike(pattern))
               .limit(10)
               .all()
    )
    return [p.name for p in results]
