# Create a basic parcel system
def calculate_volume(long, wide, high):
    return long * wide * high

def calculate_total(price, number_boxes):
    return price * number_boxes

try:
    long = float(input("Enter the length of the box:\n"))
    
    wide = float(input("Enter the width of the box:\n"))
    
    high = float(input("Enter the height of the box:\n"))
    
    number_boxes = int(input("Enter the number of boxes:\n"))
    
    volume = calculate_volume(long, wide, high)
    
    if volume < 1000000:
        price = 100
    elif volume >= 1000000 and volume <= 5000000:
        price = 300
    else:
        price = 500
        
    total_price = calculate_total(price, number_boxes)

    print("-----------------------------------")
    print("CUBIC CENTIMETERS PER BOX:", volume)
    print("NUMBER OF BOXES TO SEND:",  number_boxes)
    print("-----------------------------------")
    print("TOTAL TO PAY:", total_price)

except ValueError:
    print("Only numerical values can be entered")