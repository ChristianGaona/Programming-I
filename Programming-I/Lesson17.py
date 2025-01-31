a = 2023
while a > 1600:
    a -= 1
    #a = a -1
    if a%100 == 0:
        continue
    if a < 1980:
        break
    if a%4 == 0:
        print(a)
else:
    print("...and those are the leap years")