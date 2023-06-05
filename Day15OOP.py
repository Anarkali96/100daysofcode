class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price


    def get_data(self):
        self.name=input('Enter the name')
        self.price=input('Enter the price')


    def put_data(self):
        print(self.name)
        print(self.price)

p1=Product("","")
p1.get_data()
p1.put_data()