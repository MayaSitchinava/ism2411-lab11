#Reflection Questions:
#1. Use .get() when a key might be missing and you want a default value without crashing your program. 
# Use bracket notation when a missing key means there is a bug and you want the program to stop and show an error.
#2. This pattern is like an Excel PivotTable or SUMIFS formula. The Python version is better for large datasets 
# because it handles millions of rows instantly, automates the process, and prevents manual spreadsheet errors.

#Exercise 1
customer_one = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print(customer_one["name"])
print(customer_one["email"])
print(customer_one["tier"])
print(customer_one["ytd_spend"])
print("Full dict:", customer_one)

#Exercise 2
customer_one["phone"] = "555-0192"
print("After adding phone:", customer_one)

customer_one["tier"] = "platinum"
print("after adding tier:", customer_one)

del customer_one["email"]
print("After deleting email:", customer_one)

#Exercise 3
email_result = customer_one.get("email", "no email on file")
print("Safe lookup using .get():", email_result)

try:
    print(customer_one["email"])
except KeyError:
    print("Caught KeyError: 'email' key does not exist in dictionary.")

#Exercise 4
for key, value in customer_one.items():
    print(f"{key}: {value}")

#Exercise 5 
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

current_tier = customer_one.get("tier", "bronze")
discount_rate = tier_discounts.get(current_tier, 0)

purchase_amount = 200
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {current_tier} Discount Rate: {discount_rate * 100}% Final Price: ${final_price:.2f}")

#Exercise 6 
customers = [
    {"name": "Bob Jones", "tier": "silver"},
    {"name": "Charlie Brown", "tier": "gold"},
    {"name": "Diana Prince", "tier": "bronze"}
]

purchase_total = 300
for cust in customers:
    tier = cust.get("tier", "bronze")
    rate = tier_discounts.get(tier, 0)
    discount_amount = purchase_total * rate 
    print(f"Name: {cust['name']} | Tier: {tier} | Discount Amount: ${discount_amount:.2f}")

#Exercise 7 
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
    "Tool X": {"price": 19.99, "stock": 14}
}

for product_name, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK ALERT: {product_name} (Only {info['stock']}left in stock)")

#Exercise 8 
transactions = [
     {"region": "South", "amount": 300},
      {"region": "North", "amount": 150},
      {"region": "South", "amount": 200},
      {"region": "East", "amount": 450},
      {"region": "North", "amount": 50}  
]

region_summary = {}
for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    region_summary[reg] = region_summary.get(reg,0) + amt

for reg in sorted(region_summary.keys()):
    print(f"{reg}: {region_summary[reg]}")