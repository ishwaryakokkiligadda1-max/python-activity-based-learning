
# Hospital Billing and Patient Classification

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate billing constraints
if age < 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid input! Age and charges cannot be negative.")

else:
    total = consultation + diagnostic + treatment

    # Apply concession
    if age >= 60:
        concession = total * 0.20
    elif total >= 10000:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    # Patient classification
    if final_bill <= 5000:
        category = "Low Payment"
    elif final_bill <= 15000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Total Charges: Rs.", round(total, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Patient Classification:", category)

