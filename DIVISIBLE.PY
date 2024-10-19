x=int(input("Enter the value:"))
last_digit=x%10
print("last_digit",(x,last_digit))
if(last_digit%3==0):
    print("last_digit is divisible by 3")
else:
    print("last_digit is not divisible by 3")