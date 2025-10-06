'''
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

Example

>>> string = "abracadabra"
You can access an index by:

>>> print string[5]
a

'''

def mutate_string(string, position, character):
    s=list(string)
    s[position]=character
    s_new=''.join(s)
    return s_new

line=input("enter the string : ")
index=int(input("enter the position : "))
char=input("enter the character : ")
print(mutate_string(line,index,char))

#or

new_str=line[:index]+char+line[index+1:]
print(new_str)