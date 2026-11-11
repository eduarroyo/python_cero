def to_celsius(farenheit_temperature: float):
    return (farenheit_temperature-32)*5/9

def to_farenheit(celsius_temperature: float):
    return celsius_temperature*9/5 + 32