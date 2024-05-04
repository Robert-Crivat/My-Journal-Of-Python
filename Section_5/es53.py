score= input().split()

for n in range(0,len(score)):
    score[n] = int(score[n])

print(min(score))
print(max(score))