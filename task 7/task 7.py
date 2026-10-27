
# Retail Billing with Multiple Discount Rules

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/electronics/clothing): ").lower()
    price = float(input("Enter price: Rs. "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity!")
        continue

    amount = price * quantity

    # Category-specific tax
    if category == "food":
        tax_rate = 0.05
    elif category == "electronics":
        tax_rate = 0.18
    elif category == "clothing":
        tax_rate = 0.12
    else:
        tax_rate = 0.10

    tax = amount * tax_rate
    subtotal += amount
    total_tax += tax

    print("Product:", name)
    print("Amount: Rs.", round(amount, 2))
    print("Tax: Rs.", round(tax, 2))

# Threshold discount
if subtotal >= 5000:
    discount_rate = 0.15
elif subtotal >= 2000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate

# Maximum discount limit
max_discount = 1000
discount = min(discount, max_discount)

grand_total = subtotal + total_tax - discount

print("\n========== ITEMIZED INVOICE ==========")
print("Subtotal       : Rs.", round(subtotal, 2))
print("Total Tax      : Rs.", round(total_tax, 2))
print("Discount       : Rs.", round(discount, 2))
print("Grand Total    : Rs.", round(grand_total, 2))
print("======================================")

