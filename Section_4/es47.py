line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
abc = ["a", "b", "c"]
map = [line1,line2,line3]

t = input()
l = t[0].lower()

lp = abc.index(l)
np = int(t[1])-1
map[lp][np] = "X"
print(f"\n{line1} \n {line2} \n {line3}")

