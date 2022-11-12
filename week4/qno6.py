data = input("Enter the temperature in Celsius: ")

def farenheit():
    farenheit = (data1 * 9/5) + 32
    print ("%.1f°C is equivalent to %.1f°F" %(data1,farenheit))

length = len(data)
data1 = float(data[:length-1])
if data[-1].upper()=="C":
    farenheit()
else:
    print("Error!")