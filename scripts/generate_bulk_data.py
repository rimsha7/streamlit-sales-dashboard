import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Number of rows you want
num_rows = 10000

regions = ["East", "West", "North", "South"]
products = ["Laptop", "Mobile", "Tablet", "Monitor", "Keyboard"]
customers = ["Customer A", "Customer B", "Customer C", "Customer D", "Customer E"]

start_date = datetime(2024, 1, 1)

data = []

for i in range(num_rows):
    order_date = start_date + timedelta(days=random.randint(0, 365))
    sales = random.randint(500, 10000)
    profit = random.randint(50, 3000)

    data.append({
        "Order_ID": i + 1,
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Region": random.choice(regions),
        "Product": random.choice(products),
        "Customer": random.choice(customers),
        "Sales": sales,
        "Profit": profit
    })

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)

df.to_csv("data/sales_bulk_data.csv", index=False)

print("Bulk data created successfully: data/sales_bulk_data.csv")