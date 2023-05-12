# #Write a code to show the use of recurssion
# import sys
# sys.setrecursionlimit(150)
# i=1
# def life():
#     global i
#     i=i+1
#     print(i)
#     print('Hello')
#     life()
#
# life()
#


#Write a code to write factorial of a number using recursion
# a=int(input('Enter a number'))

def fact(n):
     if n==0:
         return 1

     return n * fact(n-1)


ans=fact(5)
print(ans)






