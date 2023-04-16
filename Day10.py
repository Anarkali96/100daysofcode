#To write factorial of a number
#
# a=int(input("Enter a number="))
# n=1
# if a==0 or a==1:
#     print('1')
# else:
#     for i in range(1,a+1):
#         n=i*n

    # print(n)
#print(type(n))


#Take array from user and after that for a specific value and show its index
from array import *
a=array('i',[])
n=int(input('Enter the length'))
m=0

for i in range(n):
    m=int(input("Enter the number"))
    a.append(m)
print(a)

r=0
o=int(input("Enter the number for search"))
for i in a:
    if i==o:



        print(r)
        break
    r=r+1
#By using inbuilt function
print(a.index(o))