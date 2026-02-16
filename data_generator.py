import pandas as pd
import random
import os
from datetime import datetime, timedelta

# Create 'data' folder if it doesn't exist
if not os.path.exists('../data'):
    os.makedirs('../data')

# Parameters
NUM_CUSTOMERS = 500
NUM_ORDERS = 2000
START_DATE = datetime(2024, 1, 1)

# --- 1. Generate CUSTOMERS Data ---
customers_data = []
countries = ['USA', 'UK', 'Germany', 'France', 'Canada']

for cust_id in range(1001, 1001 + NUM_CUSTOMERS):
    # Random signup date
    signup_date = START_DATE + timedelta(days=random.randint(0, 300))
    
    customers_data.append({
        'customer_id': cust_id,
        'signup_date': signup_date.strftime('%Y-%m-%d'),
        'country': random.choice(countries)
    })

df_customers = pd.DataFrame(customers_data)
# Saving to CSV
df_customers.to_csv('../data/customers.csv', index=False)
print("✅ data/customers.csv created successfully!")

# --- 2. Generate ORDERS Data ---
orders_data = []

for order_id in range(50001, 50001 + NUM_ORDERS):
    # Select a random customer
    customer = random.choice(customers_data)
    cust_id = customer['customer_id']
    cust_signup = datetime.strptime(customer['signup_date'], '%Y-%m-%d')
    
    # Order date must be AFTER the signup date
    days_after_signup = random.randint(1, 100)
    order_date = cust_signup + timedelta(days=days_after_signup)
    
    # Generate random revenue amount
    amount = round(random.uniform(20.0, 500.0), 2)
    
    orders_data.append({
        'order_id': order_id,
        'customer_id': cust_id,
        'order_date': order_date.strftime('%Y-%m-%d'),
        'order_amount': amount
    })

df_orders = pd.DataFrame(orders_data)
# Saving to CSV
df_orders.to_csv('../data/orders.csv', index=False)
print("✅ data/orders.csv created successfully!")