print("Enter the base of the triangle:")
base = int(input())  # Ask the user to enter an integer value for the base.

print("Enter the height of the triangle:")
height = int(input())  # Now the value of the height will enter.

area = (base * height) / 2  # Calculate the area of the triangle using the formula.

# Show the result of the calculation using a text string of that includes the calculated value.
print("The area of the triangle is " + str(area)) 
# It can also be expressed in the following way:
print(f"The area of the triangle is {area}")  # The f-string allows you to insert variables within a text string.