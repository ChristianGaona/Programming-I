# Cycle to find cycling years
year = int(input("Enter a initial cycle year: "))
for y in range(year, 2025):
    if y%4 ==0:
        print(y)