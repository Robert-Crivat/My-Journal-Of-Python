for n in range(1, 101):
    if((n % 5 == 0) and (n % 3 == 0)):
        print("\nFizzBuzz")
    elif(n % 3 == 0):
        print("\nFizz")
    elif(n % 5 == 0):
        print("\nBuzz")
    else:
        print(f"\n{n}")