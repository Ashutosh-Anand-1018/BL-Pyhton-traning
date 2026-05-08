def convert_to_farenheit(celsius:int):
    """
    This function takes a temperature in Celsius and converts it to Fahrenheit.
    """
    farenheit = (celsius * 9/5) + 32
    return farenheit
temperature = int(input("Enter the temperature in Celsius: "))
farenheit = convert_to_farenheit(temperature)
print(f"Temperature in Fahrenheit is: {farenheit:.1f} for celsius {temperature:.1f}")