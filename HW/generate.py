import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["price", "discount", "quantity", "name"]

def generate_row():

    return {
        "price": random.randint(0, 100),
        "discount": round(random.uniform(1.5, 9.9), 2),
        "quantity": random.randint(0, 100),
        "name": random.choice(["iPhone 17", "iPhone 17 Pro Max", "iPhone 17 Pro"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

