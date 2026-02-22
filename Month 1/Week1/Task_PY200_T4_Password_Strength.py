password = input("Enter your password to check the strength : ")
haveDigit = False
haveUppercase = False
haveLowercase = False


for i in password:
    if i.isupper():
        haveUppercase = True
    elif i.islower():
        haveLowercase = True
    elif i.isdigit():
        haveDigit = True
    elif(haveUppercase and haveLowercase and haveDigit):
        print("Valid password.(Strong)")


if (len(password)>=8 and (haveUppercase and haveLowercase and haveDigit)):
    print("Valid password.(Strong)")   
else:
    print("Invalid password (WEAK)")

