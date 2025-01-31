try:
    # Code that can generate an error
    
    result = 5/0
    # Will try to divide by zero, but will not be able to
    print("The result is", result)
except ValueError: # Invalid value for the expected value
    print("The value entered is incorrect")
except ZeroDivisionError: # This exception it happends when you try to divide by zero
    print("You cant divide by zero")
except:
    # Code that runs if an exception occurs
    print("An error ocurred, try again")