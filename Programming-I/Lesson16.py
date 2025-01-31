n = int(input("Enter the number you want to multiply: "))
n2 = 1
print(f"Multiplication table of the {n}:")
while n2 <= 10:
    print(f"{n} x {n2} = {n * n2}")
    n2 += 1