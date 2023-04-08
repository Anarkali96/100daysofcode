#To prin a certain pat
#cha=[1,2,3,4]
# i=1
# while i<5:
#     for j in range(i,5):
#         print(j,end="")
#     print()
#     i+=1
cha=[1,2,3,4]
#print(type(cha[1]))

for i in cha:
    j=i-1
    for j in cha[j:]:
        print(j,end="")
    print()

# Name=[1,2,3,4]
# for i in Name:
#
#     print(Name[i-1:])