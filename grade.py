num,A,B,C,D,E,F,G=0,0,0,0,0,0,0,0

grade=[]

while num>=0 and num<101:
    num=int(input("Input Grades: "))
    grade.append(num)
for i in range (len(grade)):
    if grade[i]>=96 and grade[i]<=100:
        A+=1
    elif grade[i]>=91 and grade[i]<=95:
        B+=1
    elif grade[i]>=86 and grade[i]<=90:
        C+=1
    elif grade[i]>=80 and grade[i]<=85:
        D+=1
    elif grade[i]>=75 and grade[i]<=79:
        E+=1
    elif grade[i]>=21 and grade[i]<=74:
        F+=1
    elif grade[i]>=0 and grade[i]<=20:
        G+=1

print('A-', A)
print('B-', B)
print('C-', C)
print('D-', D)
print('E-', E)
print('F-', F)
print('G-', G)