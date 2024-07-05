FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temprature = int(input("Enter the temperature to convert: "))
type_of_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

match type_of_temp:
    case "F":
        result = convert_to_celsius(temprature)
        print(f"{temprature}°F is {result}°C")
    case "C":
        result = convert_to_fahrenheit(temprature)
        print(f"{temprature}°C is {result}°F")

