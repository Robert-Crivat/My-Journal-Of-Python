#************************************************************************************************

#   MATCH DOESN'T SHOWED UP BUT I CODED IN C++ AND I REMEMBERED SWITCH CASE SO I IMPLEMENTED THAT BECAUSE I LIKE MORE TO USE THIS FILTER IN THIS SITUATION.

#************************************************************************************************
print("Welcome to python pizza !")
size = input("What size pizza do u want ? (Small = S, Medium = M, Large = L)") 
add_pepperoni = input("Do you want pepperoni ? (Y or N)")
extra_cheese = input("Do you want extra cheese ? (Y or N)")

match size :
    case "S":
        bill = 15
        if(add_pepperoni == "Y"):
            bill += 2
            if(extra_cheese == "Y"):
                bill += 3
    case "M":
        bill = 20
        if(add_pepperoni == "Y"):
            bill += 3
            if(extra_cheese == "Y"):
                bill += 1
    case "L":
        bill = 25
        if(add_pepperoni == "Y"):
            bill += 3
            if(extra_cheese == "Y"):
                bill += 1

print(f"Your ordfer is {bill} $")