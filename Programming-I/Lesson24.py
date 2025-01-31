# Make a system that separates phone numbers by area codes
try:
    print("Enter the phone numbers separated by a comma(','):")
    telephones = input()
    tels = telephones.split(",")

    guaymas = 0
    hermosillo = 0
    obregon = 0
    other = 0

    for t in tels:
        if t.startswith("622"):
            guaymas += 1
        elif t.startswith("644"):
            obregon += 1
        elif t.startswith("662"):
            hermosillo += 1
        else:
            other += 1

    print(f"Exist {guaymas} numbers of Guaymas")                    
    print(f"Exist {obregon} numbers of Obregón")
    print(f"Exist {hermosillo} numbers of Hermosillo")
    print(f"Exist {other} numbers of another cities")
    
except:
    print("An error occurred")    