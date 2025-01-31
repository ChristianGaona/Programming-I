try:
    list = ["Oscar", "Martin", "César", "Pedro", "Christian", "Sebastian", "Julian", "Miguel", "Akane"]
    a = list[3]
    print(a)
    
    list.sort()
    print(list)
    
    list.reverse()
    print(list)
    
    animals = "dog cat bird rabbit hamster"
    list_animals = animals.split()
    print(list_animals)
    
    if animals.startswith("ch"):
        print("It starts with ch")
    else:
        print("It does not starts with ch")    
    
except ValueError:
    print("Invalid value")    
except Exception as error:
    print("An error occurred")