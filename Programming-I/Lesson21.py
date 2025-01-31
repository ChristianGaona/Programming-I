# Develop a system to calculate the average of a list of numbers
def calculate_average(list_numbers):
    sum = 0
    for n in list_numbers:
        sum += n
    return sum/len(list_numbers)    

numbers = []

while len(numbers) < 20:
    
    print("Enter a number: ")
    
    numbers.append(int(input()))
else:
    print(f"The average of the numbers is {calculate_average(numbers)}")