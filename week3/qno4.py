BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
set_password = input("Enter your password(must be 8-12 characters): ")
check_password = input("Re-enter your password: ")
if 8<=len(set_password)<=12 and set_password==check_password:
    if set_password not in BAD_PASSWORDS and check_password not in BAD_PASSWORDS:
        print("Password set")
    else:
        print("error")  
else:
    print ("error")    