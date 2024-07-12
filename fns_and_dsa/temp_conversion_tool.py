def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

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
    main()

