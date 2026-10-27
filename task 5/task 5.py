
# Multi-Plan Telecommunications Cost Optimization

data = []

n = int(input("Enter number of mobile plans: "))
usage = float(input("Enter required data usage (GB): "))
days = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

for i in range(n):
    print("\nEnter details for Plan", i + 1)

    name = input("Plan name: ")
    price = float(input("Plan price (Rs.): "))
    data_limit = float(input("Data limit (GB): "))
    validity = int(input("Validity (days): "))
    extra_rate = float(input("Extra charge per GB (Rs.): "))

    excess = max(0, usage - data_limit)
    total_cost = price + excess * extra_rate

    print("Excess data:", excess, "GB")
    print("Total cost: Rs.", round(total_cost, 2))

    if (validity >= days and total_cost <= budget):
        data.append((name, total_cost, data_limit, validity))

print("\n--- Plan Comparison Result ---")

if data:
    data.sort(key=lambda x: (x[1], -x[2], -x[3]))

    for plan in data:
        print(plan[0], "- Total Cost: Rs.", round(plan[1], 2))

    best = data[0]
    print("\nMost Economical Eligible Plan:", best[0])
    print("Total Cost: Rs.", round(best[1], 2))
else:
    print("No eligible plan found within the budget.")

