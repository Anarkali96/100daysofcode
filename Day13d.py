#Write a code to print the factorial of a number
a=int(input("Enter the number"))
z=1
if a==0:
    print(1)
if a==1:
    print(1)

else:

    for i in range(1,a+1):
        z=i*z
    print(z)