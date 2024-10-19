Num=int(input("Enter the number:"))
flag=0
for i in range(2,Num):
    if(Num%i==0):
        flag=1
        break
    if(flag==1):
        print("Not prime")
    else:
        print("Prime")