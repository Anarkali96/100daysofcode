#check if number is prime or not day8
import math as m
n=int(input("Enter a no="))
r=range(2,n)
for i in r:
    if n%i==0:
        print("Not prime")
        break

else:
    print("Prime")

