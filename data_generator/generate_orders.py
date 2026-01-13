import time
import json
from utils import generate_order

def main():
    print("Starting order generator...\n")

    while True:
        order = generate_order()
        print(json.dumps(order))
        time.sleep(2)  # simulate real-time events


if __name__ == "__main__":
    main()
