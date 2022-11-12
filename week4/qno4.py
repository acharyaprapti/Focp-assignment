def remove():
    user = input("Enter a string: ")
    length = len(user)
    last = user [:length -1]
    if len(last)<=3:
        print(user)
    else:
        print("Return: ", last)


remove()    