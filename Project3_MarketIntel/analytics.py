import sqlite3

def get_market_summary():
    conn = sqlite3.connect('market_intel_india.db')
    cursor = conn.cursor()
    
    # Complex Query: Aggregating prices and calculating fluctuation
    query = """
    SELECT 
        p.name, 
        p.category, 
        ROUND(AVG(pl.price_inr), 2) as avg_price,
        ROUND(MAX(pl.price_inr) - MIN(pl.price_inr), 2) as fluctuation
    FROM products p
    JOIN price_log pl ON p.id = pl.product_id
    GROUP BY p.name
    ORDER BY avg_price DESC
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print(f"\n{'Product Name':<20} | {'Category':<15} | {'Avg Price':<12} | {'Change'}")
    print("-" * 65)
    for row in rows:
        # Formatting with the Indian Rupee symbol
        print(f"{row[0]:<20} | {row[1]:<15} | ₹{row[2]:<11} | ₹{row[3]}")
    conn.close()

if __name__ == "__main__":
    get_market_summary()