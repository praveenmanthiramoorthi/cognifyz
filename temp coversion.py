def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temp_input = input("Enter the temperature (e.g., 100C or 212F): ").strip()

if temp_input[-1].upper() == 'C':
    celsius = float(temp_input[:-1])
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
elif temp_input[-1].upper() == 'F':
    fahrenheit = float(temp_input[:-1])
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
else:
    print("Invalid input. Please enter temperature with unit (e.g., 100C or 212F).")
