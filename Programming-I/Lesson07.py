age = int(input("How old are you? "))
if (age >= 18 and age < 70):  # If the age admitted is greater than or equal to 18 but less than 70
    print("If you can apply for a driver's license")
else:  # If you don't reach 18 or over 70
    print("You can't apply for a driver's license")


color = input("Mention a color of the Japanesse flag: ")
if (color == "red" or color == "white"):  # Asks if the data entered is the same as expected
    print("That color is on the Japanesse flag")
else:  # If the color entered is neither of the two
    print("That color is not on the Japanesse flag")