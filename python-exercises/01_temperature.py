temperature=float(input("Enter the temperature: "))
unit=input("Enter the unit (C for Celsius, F for Fahrenheit): ")
if unit.upper() == 'C':
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit}°F")
elif unit.upper() == 'F':
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius}°C")
else:
    print("Invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")
 