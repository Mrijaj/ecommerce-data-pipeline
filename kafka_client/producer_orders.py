import json
import time
from kafka import KafkaProducer          # ✅ FIXED
from data_generator.utils import generate_order

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Kafka Order Producer started...")

while True:
    order = generate_order()
    producer.send("orders", order)
    print(f"Sent: {order}")
    time.sleep(2)
