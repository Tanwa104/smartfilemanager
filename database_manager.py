import sqlite3
from datetime import datetime

def setup_db():
    conn = sqlite3.connect('market_intel_india.db')
    cursor = conn.cursor()
    # Table 1: Products
    cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                      (id INTEGER PRIMARY KEY, name TEXT, category TEXT)''')
    # Table 2: Price Logs in INR
    cursor.execute('''CREATE TABLE IF NOT EXISTS price_log 
                      (id INTEGER PRIMARY KEY, product_id INTEGER, 
                       price_inr REAL, timestamp TEXT,
                       FOREIGN KEY(product_id) REFERENCES products(id))''')
    conn.commit()
    conn.close()

def insert_price(name, category, price):
    conn = sqlite3.connect('market_intel_india.db')
    cursor = conn.cursor()
    
    # Check if product exists (Upsert logic)
    cursor.execute("SELECT id FROM products WHERE name = ?", (name,))
    result = cursor.fetchone()
    
    if result:
        product_id = result[0]
    else:
        cursor.execute("INSERT INTO products (name, category) VALUES (?, ?)", (name, category))
        product_id = cursor.lastrowid
    
    # Insert the price in INR
    cursor.execute("INSERT INTO price_log (product_id, price_inr, timestamp) VALUES (?, ?, ?)", 
                   (product_id, price, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_db()
    print("✅ Indian Market Database Initialized.")