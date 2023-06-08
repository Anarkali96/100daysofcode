#Multilevel Inheritance

class A:
    def method_a(self):
        print('We have print A')

class B(A):
    def method_b(self):
        print('We haved to print B')

class C(B):
    def method_c(self):
        print('we have to print C')

cobject=C()
cobject.method_a()
cobject.method_b()
cobject.method_c()