#!/bin/bash

# Ensure Git Bash handles Indian characters correctly
export LANG=en_IN.UTF-8

# Configuration
DB_NAME="market_intel_india.db"
LOG_FILE="market_scan.log"

echo "------------------------------------------------"
echo "🇮🇳 INDIAN MARKET INTELLIGENCE SYSTEM"
echo "------------------------------------------------"
echo "Scan Started at: $(date)" | tee -a $LOG_FILE

# 1. Initialize the Database via Python
echo "[Step 1] Initializing Database..."
python -c "from database_manager import setup_db; setup_db()"

# 2. Simulate Dynamic Data Ingestion
# We will simulate scanning 5 different Indian Tech Services
echo "[Step 2] Scanning Live Market Prices..."

PRODUCTS=("Cloud-Compute-IN" "Domain-Registration" "SMS-Gateway-India" "Payment-API" "CDN-Mumbai")
CATEGORIES=("Infrastructure" "Web-Services" "Telecom" "FinTech" "Networking")

for i in {0..4}
do
    # Generate a random price between ₹500 and ₹5000
    RAND_PRICE=$(( ( RANDOM % 4500 )  + 500 ))
    NAME=${PRODUCTS[$i]}
    CAT=${CATEGORIES[$i]}

    echo ">>> Found: $NAME | Category: $CAT | Price: ₹$RAND_PRICE" | tee -a $LOG_FILE
    
    # Dynamically pass Bash variables into the Python insertion function
    python -c "from database_manager import insert_price; insert_price('$NAME', '$CAT', $RAND_PRICE)"
done

# 3. Trigger the Analytics Engine
echo "[Step 3] Running Complex SQL Analytics..."
echo "------------------------------------------------"
python analytics.py

echo "------------------------------------------------"
echo "✅ Scan Complete. Logs saved to $LOG_FILE"