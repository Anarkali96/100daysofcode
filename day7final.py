#Day7
#Writing pattern 1234 234 34 4
# z=[1,2,3,4]
# for i in z:
#     i=i-1
#     for i in range(i,len(z)):
#         print(z[i],end="")
#
#
#     print()
# z='1235'
# for i in range(len(z)):
#     for i in range(i,(len(z))):
#         print(z[i],end="")
#
#     print()
x='ABCD'
y='PQR'
for i in range(len(x)):
    print(x[0:i+1]+y[i:])
print()

# y='MADAM' :-1])
#
# if x==y:
#     print('Palindrom')
# else:
#     print('Not Palindrom')
# x=int(input('Enter the number'))
# i=1
# fact=1
# if x==0 or x==1:
#     print(fact)
# else:
#     while i<=x:
#         fact=i*fact
#         i=i+1
#     print(fact)