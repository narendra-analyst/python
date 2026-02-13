#1.nested if condition
userName="narendra"
userPassword="narendra@15"
ch1=str(input("enter userName:"))
ch2=str(input("enter userPassword:"))
if ch1==userName:
    if ch2==userPassword:
        print("login successful")
    else:
        print("password incorrect")
else:
    print("name and password is invalid")
#2.
userName="vijay"
userPassword="vijay@22"
ch1=str(input("enter userName:"))
ch2=str(input("enter userPassword:"))
if ch1==userName:
    if ch2==userPassword:
        print("login successful")
    else:
        print("password incorrect")
else:
    print("name or password is invalid")
