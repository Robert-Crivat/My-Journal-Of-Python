#if else statment
if(int(input("What is your height in cm ?")) >= 120):
    print("U can ride the rollercoaster!")
    age = int(input("Insert your age : "))
    if(age < 12):
        print("u need to pay 5$")
        bill = 5
    elif(age < 18): 
        print("u need to pay 7$")
        bill = 7
    else :
        print("u need to pay 12$")
        bill = 12
    if (str(input("you want a photo ? (Y or N)")) == "Y"):
        bill += 3
    print(f"your bill is {bill}$")
else :
    print("U can't ride the rollercoaster!")