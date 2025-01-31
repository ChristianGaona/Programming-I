def calculate_tax(type, value):
    if type == "VAT":  # The tax type is VAT (Value-Added Tax) of the 16%.
        return float(value) * 0.16
    # elif = else if
    elif type == "IT":  # The tax type is IT (Income Tax) of the 33%.
        return float(value) * 0.33
    elif type == "ET":  # The tax type is ET (Excise Tax) of the 15%.
        return float(value) * 0.15
    elif type == "PT":  # The tax type is PT (Payroll Tax) of the 10%.
        return float(value) * 0.10
    else:  # If it is none of these types then it returns zero.
        return 0
print("Write tax type: ")
type = input()

value = input("Enter the value:\n")
tax = calculate_tax(type.upper(), value)
total = float(value) + float(tax)

print("The price is", value)
print("The tax is", tax)
print("The total is", total)