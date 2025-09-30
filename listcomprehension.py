'''
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to . Here, 0<=i<=x ,0<=j<=y , 0<=k<=z . Please use list comprehensions rather than multiple loops, as a learning exercise.

'''
# answer

x=int(input("enter the x value : "))
y=int(input("enter the y value : "))
z=int(input("enter the z value : "))
n=int(input("enter the n value : "))
out=[]

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if (i+j+k)!=n:
                out.append([i,j,k])
print(out)