FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature_to_convert = float(input("Enter the temperature to convert: "))
temperature_units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper

def convert_to_celsius(fahrenheit):
    temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR    
    print(f"{fahrenheit}°F is {temp}°C")

def convert_to_fahrenheit(celsius):
    temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {temp}°F")
if temperature_to_convert.is_integer:
    if temperature_units == "F":
        convert_to_celsius(temperature_to_convert)
    elif temperature_units == "C":
        convert_to_fahrenheit(temperature_to_convert)
    else:
        print(f"Invalid temperature.")
else:
    print(f"Invalid temperature. Please enter a numeric value.")