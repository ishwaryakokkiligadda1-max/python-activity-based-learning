
# Campus Event Financial Planning

print("Campus Event Financial Planning")

venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected participants: "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))

if (venue < 0 or equipment < 0 or catering < 0
        or transport < 0 or certificate < 0
        or participants < 0 or registration_fee < 0
        or sponsorship < 0):
    print("Invalid input! Values cannot be negative.")

else:
    # Calculate expenses
    fixed_cost = venue + equipment + transport
    variable_cost = (catering + certificate) * participants
    total_cost = fixed_cost + variable_cost

    # Calculate income
    participant_income = participants * registration_fee
    total_income = participant_income + sponsorship

    # Calculate sponsorship shortfall
    shortfall = max(0, total_cost - sponsorship)

    # Calculate minimum registrations needed
    contribution = registration_fee - catering - certificate

    print("\n--- Event Financial Report ---")
    print("Fixed Costs: Rs.", round(fixed_cost, 2))
    print("Variable Costs: Rs.", round(variable_cost, 2))
    print("Total Event Cost: Rs.", round(total_cost, 2))
    print("Participant Contributions: Rs.",
          round(participant_income, 2))
    print("Sponsorship: Rs.", round(sponsorship, 2))
    print("Total Income: Rs.", round(total_income, 2))
    print("Sponsorship Shortfall: Rs.", round(shortfall, 2))

    if total_income >= total_cost:
        print("Status: Event is financially feasible.")
        print("Surplus: Rs.", round(total_income - total_cost, 2))
    else:
        print("Status: Event is running at a loss.")
        print("Loss: Rs.", round(total_cost - total_income, 2))

    if contribution > 0:
        required = max(0, int((fixed_cost - sponsorship) /
                              contribution) + 1)
        # Correct ceiling calculation
        required = max(0, (max(0, fixed_cost - sponsorship)
                           + contribution - 1) // contribution)

        print("Minimum Registrations to Break Even:", required)

    elif fixed_cost <= sponsorship:
        print("Minimum Registrations to Break Even: 0")
    else:
        print("Break-even is not possible with this registration fee.")

