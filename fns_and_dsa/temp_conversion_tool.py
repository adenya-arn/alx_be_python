
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
