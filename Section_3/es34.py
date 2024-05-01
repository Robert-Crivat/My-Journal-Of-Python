year =int(input("insert the year u want to check : "))
if( year %4 == 0 and year %400 == 0):
    print("this is a leap year")
else : 
    print("this is not a leap year")