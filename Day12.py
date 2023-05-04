#Learning about argument
def Person(**data):
# print(name)
# print(data)
    for i,j in data.items():        print(i,j)

Person(name='Anarkali',Age=26,Edu="Mtech",City="Nagpur)