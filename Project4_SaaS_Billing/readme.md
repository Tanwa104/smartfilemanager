# 💰 SaaS Automated Billing & GST Engine

## The Problem
For any Indian startup, manual billing is a nightmare—especially when you have customers using different amounts of resources every month. Calculating tiered pricing and then adding the 18% GST manually is prone to errors. I built this to automate that entire "Finance Department" workflow.

## 🛠 How it Works
This isn't just a simple script; it's a mini-system that handles the end-to-end billing cycle:
1. **The Core Engine (`billing_engine.py`):** This is where the heavy lifting happens. It pulls usage data from SQLite and applies tiered pricing (the more a client uses, the different the rate). It then calculates the CGST and SGST (9% each) to comply with Indian tax standards.
2. **The Automation (`billing_manager`):** A Bash script that acts as the "Scheduler." In a real company, you would set this to run at midnight on the 1st of every month. It triggers the Python engine and logs the results.
3. **The Output (`generate_invoice.py`):** This takes the raw numbers and turns them into a professional, human-readable Tax Invoice.

## 🚀 Technical Achievements
- **Dynamic Pricing:** I implemented logic where the cost per hour changes based on usage thresholds.
- **Financial Accuracy:** Used precise rounding logic to ensure the GST amounts match the final total down to the paisa.
- **Relational Data:** Designed the `customer_usage.db` to track client IDs, hours used, and subscription tiers.

## 📄 What the Output Looks Like
When the system runs, it generates a professional summary like this:

=============================================
       TAX INVOICE - SAAS SERVICES
=============================================
CLIENT ID: ZYL_562 (Premium Tier)
Usage: 145.5 Hours
---------------------------------------------
Subtotal:           ₹29,642.00
CGST (9%):          ₹2,667.78
SGST (9%):          ₹2,667.78
---------------------------------------------
TOTAL AMOUNT DUE:   ₹34,977.56
=============================================

---
*Note: This project proves I can handle sensitive business logic and automate repetitive financial tasks using Python and Bash.*
