#!/bin/bash

# Ensure terminal supports Rupee symbol
export LANG=en_IN.UTF-8

echo "------------------------------------------"
echo "🚀 STARTING INDIAN BILLING PIPELINE..."
echo "------------------------------------------"

# Step 1: Initialize Database
python billing_engine.py

# Step 2: Simulate User Usage (Dynamic Insertion)
echo "📥 Ingesting Usage Events..."

SERVICES=("API_TOKEN" "CLOUD_COMPUTE" "DATA_TRANSFER")

for i in {1..15}
do
    # Pick a random service
    SELECTED_SERVICE=${SERVICES[$RANDOM % 3]}
    # Pick a random number of units (e.g., 10 to 100)
    UNITS=$(( (RANDOM % 90) + 10 ))
    
    echo "Event $i: Logged $UNITS units of $SELECTED_SERVICE"
    
    # Dynamically pass variables to Python
    python -c "from billing_engine import log_usage; log_usage(1, '$SELECTED_SERVICE', $UNITS)"
    
    # Slight delay to simulate real-time traffic
    sleep 0.2
done

# Step 3: Run the Invoice Analytics
echo "💰 Generating GST Compliant Invoice..."
python generate_invoice.py

echo "✅ Process Finished Successfully."