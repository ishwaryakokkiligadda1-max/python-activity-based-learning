
# Employee Payroll and Deduction Analysis

name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentives = float(input("Enter incentives: "))

if basic < 0 or allowances < 0 or overtime < 0 or incentives < 0:
    print("Invalid input! Salary values cannot be negative.")

else:
    gross = basic + allowances + overtime + incentives

    # Progressive deductions
    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 50000:
        deduction = 20000 * 0.05 + (gross - 20000) * 0.10
    else:
        deduction = 20000 * 0.05 + 30000 * 0.10 + (gross - 50000) * 0.20

    net_salary = gross - deduction

    # Formatted salary statement
    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name :", name)
    print("Basic Pay     : Rs.", round(basic, 2))
    print("Allowances    : Rs.", round(allowances, 2))
    print("Overtime      : Rs.", round(overtime, 2))
    print("Incentives    : Rs.", round(incentives, 2))
    print("--------------------------------------")
    print("Gross Salary  : Rs.", round(gross, 2))
    print("Deductions    : Rs.", round(deduction, 2))
    print("Net Salary    : Rs.", round(net_salary, 2))
    print("======================================")
ishwry
