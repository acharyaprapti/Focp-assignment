import statistics
six_temp = []
formean=[]
for x in range(1,7):
    ask = input(f"Enter {x} datas : ")
    if ask[-1].upper()=="C":
        length = len(ask)
        temp = float(ask[:length-1])
        six_temp.append(ask)
        formean.append(temp)
    else:
        print("Error!")
        break
print("The maximum temperature is: ", max(six_temp))
print("The minimun temperature is: ", min(six_temp))
print("The mean is: ", statistics.mean(formean))
