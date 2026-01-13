import sqlite3
from datetime import datetime

def init_billing():
    conn = sqlite3.connect('billing_india.db')
    cursor = conn.cursor()
    
    # 1. Create Users Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY, name TEXT, city TEXT, plan TEXT)''')
    
    # 2. Create Usage Logs Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS usage_logs 
                      (id INTEGER PRIMARY KEY, user_id INTEGER, service TEXT, 
                       units INTEGER, timestamp TEXT,
                       FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    # Pre-populate with a sample Indian Startup Client
    cursor.execute("INSERT OR IGNORE INTO users (id, name, city, plan) VALUES (1, 'Zylker Tech Bangalore', 'Karnataka', 'Enterprise')")
    
    conn.commit()
    conn.close()

def log_usage(user_id, service, units):
    conn = sqlite3.connect('billing_india.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usage_logs (user_id, service, units, timestamp) VALUES (?, ?, ?, ?)",
                   (user_id, service, units, datetime.now().isoformat()))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_billing()
    print("✅ Indian Billing Database Initialized.")