def upperlower():
    user = input("Enter words: ")
    count = 0
    num = 0
    for x in user:
        if x.isupper():
            count = count + 1
        if x.islower():
            num = num + 1
    print("The number of uppercase in%s is %d and lowercase is %d." %(user, count, num))
upperlower()                