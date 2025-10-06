'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

'''
def sub_count(string,substr):
    count=0
    l=len(substr)
    i=0
    while(i<=(len(string)-l)):
        if(string[i:i+l]==substr):
            count+=1
        i+=1
    print("substring count = ",count)

line=input("enter the string : ")
subline=input("enter the substring : ")
sub_count(line,subline)
print(line.count(subline))  #inbuilt function
