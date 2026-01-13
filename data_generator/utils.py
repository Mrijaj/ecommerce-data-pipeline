from faker import Faker
import random
from datetime import datetime

fake = Faker()

PRODUCTS = [
    ("Laptop", 55000),
    ("Headphones", 3000),
    ("Keyboard", 1500),
    ("Mouse", 800),
    ("Monitor", 12000),
    ("Smartphone", 25000),
]

CITIES = ["Pune", "Mumbai", "Bangalore", "Delhi", "Hyderabad"]


def generate_order():
    product_name, price = random.choice(PRODUCTS)

    return {
        "order_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "product": product_name,
        "price": price,
        "city": random.choice(CITIES),
        "order_time": datetime.utcnow().isoformat()
    }
