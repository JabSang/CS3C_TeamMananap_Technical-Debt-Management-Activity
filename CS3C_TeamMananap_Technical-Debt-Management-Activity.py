def calculate_sss(salary):
    #Calculate SSS deduction based on salary.
    return 1200

def calculate_philhealth(salary):
    #Calculate PhilHealth deduction based on salary.
    return (salary * 0.05) / 2

def calculate_pagibig(salary):
    #Calculate Pag-IBIG deduction (fixed value).
    return 100

def calculate_tax(salary):
    #Calculate tax deduction based on salary and fixed tax for simplicity
    return 1875  

def compute_deductions(salary):
    #Compute all deductions and net salary.
    sss = calculate_sss(salary)
    philhealth = calculate_philhealth(salary)
    pagibig = calculate_pagibig(salary)
    tax = calculate_tax(salary)

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    return sss, philhealth, pagibig, tax, deductions, net_salary

def get_salary_input():
    #Get and validate salary input from user.
    while True:
        try:
            salary = float(input("Enter your monthly salary: "))
            if salary <= 0:
                print("Salary must be a positive number.")
            else:
                return salary
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    #Main function to run the salary deduction calculation.
    salary = get_salary_input()

    # Compute deductions
    sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(salary)

    # Display results
    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

# Run the program
if __name__ == "__main__":
    main()
