
# Manufacturing Cost and Profitability Analysis

product = input("Enter product name: ")
quantity = int(input("Enter quantity produced: "))

material = float(input("Enter material cost per unit: Rs. "))
labour = float(input("Enter labour cost per unit: Rs. "))
wastage = float(input("Enter wastage cost per unit: Rs. "))
machine = float(input("Enter machine cost per unit: Rs. "))
selling = float(input("Enter selling price per unit: Rs. "))
target = float(input("Enter target profit percentage: "))

if (quantity <= 0 or material < 0 or labour < 0
        or wastage < 0 or machine < 0
        or selling < 0 or target < 0):
    print("Invalid input!")
else:
    # Calculate total production cost
    cost_per_unit = material + labour + wastage + machine
    total_cost = cost_per_unit * quantity

    # Calculate revenue and profit
    revenue = selling * quantity
    profit = revenue - total_cost

    if total_cost > 0:
        profit_percent = (profit / total_cost) * 100
    else:
        profit_percent = 0 if revenue == 0 else float("inf")

    # Display report
    print("\n--- Manufacturing Report ---")
    print("Product:", product)
    print("Quantity Produced:", quantity)
    print("Cost per Unit: Rs.", round(cost_per_unit, 2))
    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Total Revenue: Rs.", round(revenue, 2))
    print("Profit/Loss: Rs.", round(profit, 2))

    if profit > 0:
        print("Status: PROFIT")
    elif profit < 0:
        print("Status: LOSS")
    else:
        print("Status: BREAK-EVEN")

    print("Profit Percentage:", round(profit_percent, 2), "%")

    if profit_percent >= target:
        print("Target Achieved!")
    else:
        print("Target Not Achieved!")

