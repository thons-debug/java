t1=(10,20,30,30,40,50)
print(t1[0:3])
print(len(t1))
print(t1.count(30))
print(10 in t1)
t2=(15,60,70)
t3=t1+t2;
print(t3)
print(sorted(t3))
print(min(t3))
print(max(t3))
t4=(1,2,3)
first,second,third=t4
print(second)
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
s1=Student("riya",23)
s1.display()
class product:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price
    def display(self):
        print(self.pname)
        print(self.price)
s2=product("phone",45345)
s2.display()

class parent:
    def parent(self):
        print("from parent class")
class Child(parent):
    def child(self):
        print("from child class")
c=Child()
c.child()
c.parent()
        
