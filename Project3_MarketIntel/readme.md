# 📊 Market Intelligence & Price Tracker

## Why I built this
During my project work, I realized that cloud service prices in India (like domain hosting or VPS) change frequently. I wanted a way to stop checking websites manually and start tracking data like a professional. This tool simulates a "Market Intelligence" bot that a company would use to keep an eye on competitors.

## 🛠 What's inside?
I split this project into three logical parts to keep the code clean:
1. **The Scanner (`market_scanner`):** A Bash script that acts as the "worker." It triggers the data collection.
2. **The Database Manager (`database_manager.py`):** This is the brain. It uses Python to talk to SQLite, creating tables and making sure the data is stored correctly without duplicates.
3. **The Analytics (`analytics.py`):** This is the "Consultant" part of the code. It runs SQL queries to calculate average prices and tells us if a deal is actually "Cheap" or "Expensive" compared to the market average.

## 🚀 Technical Highlights
- **SQL Skills:** I used `GROUP BY` and `AVG()` functions in SQLite to process raw data into insights.
- **Automation:** The Bash script ensures the Python logic runs in the correct sequence.
- **Data Integrity:** I implemented logic to ensure that every time the scanner runs, it adds new timestamps so we can see price changes over time.

## 📈 Sample Analytics Output
When I run the analytics script, this is the kind of insight it produces:
| Category | Avg Price (INR) | Trend |
| :--- | :--- | :--- |
| Cloud Hosting | ₹850.00 | 🟢 Stable |
| Domain (.com) | ₹1,100.00 | 🔴 Rising |

---
*Note: This project demonstrates my ability to bridge the gap between raw data collection and business decision-making.*
