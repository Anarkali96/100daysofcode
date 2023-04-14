#Day 9
#Learning about array and how to use it

#how to make arrays
#print squares of number
from array import *
# Christ=array('I',[2,3,5,7])
# print(Christ)
#
# newarr=array(Christ.typecode,(a*a for a in Christ))
# print(newarr)



#code for an array to sort in descending order
Value=array('i',[1,2,5,7,-4,4,5])
#a=max(Value)
arr2 = [None] * len(Value)
for i in range(len(Value)):
    a=max(Value)
    #print(a,end="")
    arr2[i]=a

    Value.remove(max(Value))
print(arr2)

