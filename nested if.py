#Nested if condition
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
