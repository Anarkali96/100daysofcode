#Inheritance
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

class Digital_Product(Product):
    def __init__(self,link):
        self.link=link

    def get_link(self):
        self.link=input('Enter the product')

    def put_link(self):
        print(self.link)
ebook=Digital_Product("")
ebook.get_data()
ebook.get_link()
ebook.put_data()
ebook.put_link()