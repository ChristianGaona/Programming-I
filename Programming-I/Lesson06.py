name = input("What's your name? ")
control_number = input("Enter your control number: ")

daily_salary = int(input("What is your daily salary? "))
days_worked = int(input("Enter the number of days worked in the month: "))
monthly_salary = daily_salary * days_worked

# If the monthly salary paid is less than 5000, an extra percentage will be applied.
if monthly_salary <= 5000:
    bonus = monthly_salary * 0.15
    monthly_payment = monthly_salary + bonus
    print("\nName:",name,"\nControl number:",control_number,"\nYour total monthly salary is", monthly_payment, "including a 15% bonus.")
# If it is not less and is greater than or equal to 5000, no percentage will be applied.
else:
    print("\nName:",name,"\nControl number:",control_number,"\nYour total monthly salary is", monthly_salary)