import random
yesno=input("roll or no")
while(yesno=="y"):
    num=random.randint(1,6)
    print(num)
    yesno=input("roll or no")