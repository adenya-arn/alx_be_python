#ask user for number
number = int(input("Enter a number to see its multiplication table:"))

#multiply
for product in range(1, 11):
    result = number * product
    print(f"{number} * {product} = {result}")  






