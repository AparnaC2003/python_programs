'''
In Python, a string can be split on a delimiter.

 a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Sample Input

this is a string   
Sample Output

this-is-a-string

'''

def split_join(line):
    line=line.split(" ")
    print(line)
    line="".join(line)
    return line

line=input("enter the string : ")
result=split_join(line)
print(result)