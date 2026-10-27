
n = int(input("Enter number of months: "))
bills = []

for i in range(n):
    print("\nMonth", i + 1)
    units = float(input("Enter units consumed: "))

    # Progressive slab rates
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        energy = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    fixed = 50
    surcharge = energy * 0.05
    rebate = 20 if units < 100 else 0

    total = energy + fixed + surcharge - rebate
    bills.append(total)

    print("Energy Charge: Rs.", round(energy, 2))
    print("Fixed Charge: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", rebate)
    print("Total Bill: Rs.", round(total, 2))

print("\nMonthly Bill Comparison")

for i in range(n):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if bills[i - 1] > 0 and increase > bills[i - 1] * 0.25:
            print("Unusual increase detected!")
        elif increase > 0:
            print("Bill increased by Rs.", round(increase, 2))
        else:
            print("No increase in bill.")

