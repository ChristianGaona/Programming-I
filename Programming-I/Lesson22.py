try:
    list = ["Oscar", "Martin", "Cesar"]

    # Attach an item to the end of a list
    list.append("Emiliano")
    list.append("Angel")
    list.append("Jostyn")
    print(list)

    # Insert an element in a specific position
    list.insert(3, "Dylan")
    print(list)

    # Removes an item from a list from its value
    list.remove("Angel")
    print(list)
    
    # If you try to remove an element that does not exist in the list, it will cause a Value Error
    # list.remove("Akane")
    
    # Remove an element by index
    removed = list.pop(4)
    print(removed)
    print(list)
    
    # If we do not specify the index, it will remove the last one from the list
    list.pop()
    print(list)
    
    # It can be eliminated from the last element by counting in negative
    list.pop(-2)
    print(list)
    
    # If we try to remove an index that does not exist, it will throw an error
    # list.pop(80)
    
    del list[2]
    print(list)
    
    list.append("Carlos")
    list.append("Luis")
    list.append("Ramon")
    list.insert(3, "Alexandro")
    list.append("Dahir")
    print(list)
    
    # The keyword del (delete) allows us to delete the index
    del list[2:5]
    print(list)
    
    # Delete or clear the entire list
    list.clear()
    print(list)
    
except ValueError:
    print("The value you are trying to remove does not exist")    
except IndexError:
    print("The index entered does not exist")
except:
    print("An error occurred")        