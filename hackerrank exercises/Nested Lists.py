students = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
#studets.sort()
#print(students[0][1])
tmp1 = students[0][1]
#tmp2 = students[0][0]
for i in range(1, len(students)):
    if tmp1 > students[i][1]:
        tmp1 = students[i][1]
        #tmp2 = students[i][0]
tmp4 = [["", 101.0]]
print("asd",tmp4[0][1])

for i in range(1, len(students)):
    if tmp4[0][1] == students[i][1]:
        tmp4.append([students[i][0], students[i][1]])
    if tmp1 < students[i][1] and float(tmp4[0][1]) > students[i][1]:
        tmp4 = [students[i][0], students[i][1]]
    
tmp4.sort()
for i in range(0, len(tmp4)):
    print(tmp4[i][0])
