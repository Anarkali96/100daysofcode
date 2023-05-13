#Day 14
#how to take function as an argument

def div(a,b):
    print(a/b)
# div(4,2)
# print(div(4,2))
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


div1=smart_div(div)
div1(4,2)
