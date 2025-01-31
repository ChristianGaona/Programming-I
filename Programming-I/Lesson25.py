price = []

def calculate_vat(price):
    price * .16
    try:
        while len(price) < 20:
            print("Enter a price or 'end' to finish: ")
            entrance = input().lower()
            if entrance == 'end':
                break
            else:
                price.append(float(entrance))
                
        for p in price:
            print(p)
            vat = calculate_vat(p)
            print(vat)
            print(p + vat)
                
                
    except ValueError:
        print("The value entered not is a valid number")            