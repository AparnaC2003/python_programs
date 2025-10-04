'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00

'''

n=int(input("enter the no. of students = "))
print("enter the student name and list of mark")
std_record={}
marks=[]
for i in range(n):
    name=input ("enter the name : ")
    print("enter marks")
    for j in range(3):
        marks.append(int(input()))
    std_record[name]=marks
    marks=[]
print(std_record)
average_score=0
query_name=input("enter the student name to find the average : ")
for i in std_record:
    if i==query_name:
        for j in std_record[i]:
            average_score+=j
        average_score/=3
print("average score of student ",query_name," = ",average_score)