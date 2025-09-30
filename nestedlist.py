'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

'''

# x=[[1,2],[3,4]]
# for i in x:
#     print(i[1])

std_list=[]
mark_list=[]
n=int(input("enter the no. of students"))
for i in range(n):
    name=input("enter the student name : ")
    mark=int(input("enter the mark : "))
    std_list.append([name,mark])
print(std_list)
for i in std_list:
    mark_list.append(i[1])
print("marklist : ",mark_list)
print("sorted mark_list :")
set_ml=list(set(mark_list))
set_ml.sort()
print(set_ml)
second_lowest=set_ml[1]
print("students with second lowest mark :")
for i in std_list:
    if i[1]==second_lowest:
        print(i[0])