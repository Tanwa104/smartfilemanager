import sqlite3

def generate_gst_report():
    conn = sqlite3.connect('billing_india.db')
    cursor = conn.cursor()

    # COMPLEX QUERY: 
    # 1. Joins Users and Logs
    # 2. Assigns different Rupee rates per service using CASE
    # 3. Sums them up into a Subtotal
    query = """
    SELECT 
        u.name,
        u.city,
        SUM(CASE 
            WHEN l.service = 'API_TOKEN' THEN l.units * 0.75
            WHEN l.service = 'CLOUD_COMPUTE' THEN l.units * 150.00
            WHEN l.service = 'DATA_TRANSFER' THEN l.units * 5.00
            ELSE l.units * 2.50
        END) as subtotal
    FROM users u
    JOIN usage_logs l ON u.id = l.user_id
    GROUP BY u.id
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    if not rows:
        print("No usage data found to generate invoice.")
        return

    print("\n" + "="*45)
    print("       TAX INVOICE - SAAS SERVICES       ")
    print("="*45)
    
    for row in rows:
        name, city, subtotal = row
        gst_amount = subtotal * 0.18
        total_payable = subtotal + gst_amount
        
        print(f"CLIENT: {name}")
        print(f"LOCATION: {city}, India")
        print("-" * 45)
        print(f"Subtotal:           ₹{subtotal:,.2f}")
        print(f"CGST + SGST (18%):  ₹{gst_amount:,.2f}")
        print("-" * 45)
        print(f"TOTAL AMOUNT DUE:   ₹{total_payable:,.2f}")
        print("="*45)
        print("Terms: Please pay within 7 days of issue.\n")

    conn.close()

if __name__ == "__main__":
    generate_gst_report()