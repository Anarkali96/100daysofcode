# def find(list):
#     even=0
#     odd=0
#     for i in list:
#         if i%2==0:
#             even=even+1
#         else:
#             odd=odd+1
#     # print('odd=',odd ,'even=',even)
#     # print('even=',even)
#     return even,odd
#
# xyx=[1,3,5,7,9,2]
# (even,odd)=find(xyx)
# print('even=',even)
# print('odd=',odd)
# print('Even : {} and Odd : {}'.format(even,odd))

# Write a code to take name from users and display the names which has more than 5 letters
list=[]
for i in range(5):
    z=input('Enter the name')
    list.append(z)
for i in list:
    if len(i)>=5:
        print(i)
    else:
        pass