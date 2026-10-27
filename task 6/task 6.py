
# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))
total_fare = 0

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    print("Classes: 1. Sleeper  2. AC")
    choice = int(input("Choose travel class: "))

    # Distance slab fare
    if distance <= 100:
        rate = 1
    elif distance <= 500:
        rate = 1.5
    else:
        rate = 2

    # Travel class multiplier
    if choice == 1:
        class_name = "Sleeper"
        multiplier = 1
    elif choice == 2:
        class_name = "AC"
        multiplier = 2
    else:
        print("Invalid class. Skipping passenger.")
        continue

    fare = distance * rate * multiplier

    # Age-based concession
    if age < 5:
        concession = fare
    elif age >= 60:
        concession = fare * 0.20
    else:
        concession = 0

    reservation_fee = 40
    cancellation = input("Cancel ticket? (yes/no): ").lower()

    final_fare = fare - concession + reservation_fee

    if cancellation == "yes":
        penalty = final_fare * 0.25
        final_fare = final_fare + penalty
    else:
        penalty = 0

    total_fare += final_fare

    print("\n--- Passenger Ticket ---")
    print("Name:", name)
    print("Class:", class_name)
    print("Base Fare: Rs.", round(fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Final Fare: Rs.", round(final_fare, 2))

print("\nTotal Amount for All Passengers: Rs.",
      round(total_fare, 2))

