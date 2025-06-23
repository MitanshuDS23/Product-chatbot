from app import app
from models import reset_and_seed

if __name__ == '__main__':
    with app.app_context():
        reset_and_seed()
    print("✅ Database products table has been wiped and reseeded with 100 items.")