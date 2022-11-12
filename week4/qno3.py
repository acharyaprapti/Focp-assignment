def greetings():
    user = input("Enter your name: ")
    name = user[1:].lower()
    first_letter = user[0].upper()
    full_name = first_letter + name
    print ("Hello, %s. Good to meet you!" %(full_name))

greetings()