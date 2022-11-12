import statistics
six_temp = []
formean=[]
while True:
    ask = input("Enter datas : ")
    if ask:
        if ask[-1].upper()=="C":
            length = len(ask)
            temp = float(ask[:length-1])
            six_temp.append(ask)
            formean.append(temp)
        else:
            print("Error!")
            break
    else: 
        break
print("The maximum temperature is: ", max(six_temp))
print("The minimun temperature is: ", min(six_temp))
print("The mean is: ", statistics.mean(formean))
