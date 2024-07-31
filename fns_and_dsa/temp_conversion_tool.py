'''# Define Global Conversion Factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
'''
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    print("Temperature Conversion Tool")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main() '''



FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

print('Temp conversion tool')


Temp = float(input('Enter the temperature to convert in numbers:'))
Measure = str(input('Is this temperature in Celsius or Farenheit? (C/F)').upper())



def cel_to_far(C):
    return (C * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def far_to_cel(F):
    return (F - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


if Measure == 'C':
    new_temp = f'{Temp} {Measure} is {cel_to_far(Temp)}°F'
    print (new_temp)
elif Measure == 'F':
    new_temp = f'{Temp} {Measure} is {far_to_cel(Temp)}°C'
    print (new_temp)
else:
    print('Invalid Temperature. Please enter a numeric value!!')
