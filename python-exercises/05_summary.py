"""This script reads sales data from a CSV file named 'sales.csv' and calculates:
1. The total sales amount.
2. The product with the highest total sales.
3. The average sale amount."""
import csv

total_sales = 0.0
product_totals = {}
num_sales = 0

with open('sales.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        amount = float(row['amount'])
        product = row['product']
        
        total_sales += amount
        
        if product in product_totals:
            product_totals[product] += amount
        else:
            product_totals[product] = amount
            
        num_sales += 1

average_sale = total_sales / num_sales if num_sales > 0 else 0

top_product = None
highest_sales = 0.0

for product, total in product_totals.items():
    if total > highest_sales:
        highest_sales = total
        top_product = product

print(f"Total sales amount: ${total_sales:.2f}")
print(f"The product with the highest total sales: {top_product} (${highest_sales:.2f})")
print(f"Average sale amount: ${average_sale:.2f}")