'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given "n"  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains "n". The second line contains an array A[]  of n integers each separated by a space.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5

'''

n=int(input("enter the no. of scores : "))
A=[]
print("enter the ",n," scores")
for i in range(n):
    A.append(int(input()))
print(A)
score=list(set(A))
score.sort(reverse=True)
print("runnerup score = ",score[1])
