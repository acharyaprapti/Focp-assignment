def farenheit():
    celsius = float(input("Enter the temperature in Celsius: "))
    farenheit = (celsius * 9/5) + 32
    print ("%.1f°C is equivalent to %.1f°F" %(celsius,farenheit))

farenheit()

def celsius():
    farenheit = float(input("Enter the temperature in Farenheit: "))
    celsius = (farenheit - 32) * 5/9
    print ("%.1f°F is equivalent to %.1f°C" %(farenheit,celsius))

celsius()
