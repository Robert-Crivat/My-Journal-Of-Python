def option():
    t = 0
    for n in range(2, int(input("your target number : "))+1,2):
        #if(n % 2 == 0):
        t += n
    print(t)

def option1():
    t = 0
    for n in range(2, int(input("your target number : "))+1,2):
        if(n % 2 == 0):
            t += n
    print(t)
