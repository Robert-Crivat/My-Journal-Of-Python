bmi = int(input("insert your weight in kg : "))/pow(float(input("insert your height in m : ")),2)
if(bmi < 18.5 ):
    print(f"Your bmi is {bmi}, you are underweight ")
else:
    if(bmi > 18.5 and bmi < 25):
        print(f"Your bmi is {bmi}, you have a normal weight")
    elif (bmi > 25 and bmi < 30) :
        print(f"Your bmi is {bmi}, you are slightly overweight")
    elif (bmi > 30 and bmi < 35) :
        print(f"Your bmi is {bmi}, you are obese")
    else : 
        print(f"Your bmi is {bmi}, you are clinically obese")
