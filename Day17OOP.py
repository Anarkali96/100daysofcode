#Multiple Inheritance

class A:
    def method_a(self):
        print('Method of class A')

class B:
    def method_b(self):
        print('Method of class B')

class C(A,B):
    def method_c(self):
        print('Method of class C')

Cobject=C()
Cobject.method_a()
Cobject.method_b()object.method_c()