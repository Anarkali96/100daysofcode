#Day 11
#
from array import *
arr=array('i',[1,2,3])
# arr.reverse()
# print(arr)
print(arr[: :-1])

#Create an array of 5 numbers and delete the value if index number2
arr1=array('i',[1,3,6,8,0])
arr2 = [None] * 4;
for i in arr1:
    if i==arr1[2]:
        continue
    print(i,end=" ")

