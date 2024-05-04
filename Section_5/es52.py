student_heights = input().split()
avg = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    avg += student_heights[n]
print(f"\ntotal height : {avg}\ntotal student {len(student_heights)}\navg height : {avg/len(student_heights)}")
