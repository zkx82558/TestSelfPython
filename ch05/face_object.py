'''面向对象
1、封装(安全，将方法属性包装到类里面)、继承(提高代码的复用性)、多态(提高程序的可扩展性和可维护性)
2、python支持多继承，方法重写，所有的类都默认继承object类，dir()查看类里面的属性和方法
'''

#继承，此处是一个父亲，两个儿子，以及方法重写
class Person(object): #person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):  #重写方法
        super().info()  #调用父类的方法
        print(self.stu_no)  #再调用子类的输出

class Teacher(Person):
    def __init__(self,name,age,teacher_year):
        super().__init__(name, age)  #super()表示继承和调用父类里面的方法
        self.teacher_year = teacher_year
    def info(self):  #重写方法
        super().info()  #调用父类的方法
        print(self.teacher_year)

stu=Student('张三',20,'1001')
teacher=Teacher('李四',30,10)

stu.info()  #直接从父类继承方法
teacher.info()

#此处是一个儿子两父亲，A和B继承了object,C同时继承A和B
class A(object):
    pass
class B(object):
    pass
class c(A,B):
    pass

#关于object类：
class Firend():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):  #经常重写str方法用于返回类型的描述
        return '我的名字是{0}，今年{1}岁'.format(self.name,self.age)
fir=Firend('张',20)
print(dir(fir))  #查看对象有那些属性和方法
print(fir) #我的名字是张，今年20岁  这里默认调用__str__()方法
print(type(fir)) #<class '__main__.Firend'>

#多态
class Animal(object):
    def eat(self):
        print('动物会吃')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class anther_person(object):
    def eat(self):
        print('人吃米饭')

def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Animal())
fun(anther_person())   #这里直接动态的绑定了方法，只用关心是都具有eat的行为
#如果是java的话，必须指明是父类继承才可以进行调用，不然就是错的



'''特殊的属性和方法，自带函数'''
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
x=C('jack',20)  #x是C类型的实例对象
print(x.__dict__)  #{'name': 'jack', 'age': 20}，实例对象的属性字典
print(C.__dict__)  #{'__module__': '__main__', '__init__': <function C.__init__ at 0x000001D6DDA2C268>, '__doc__': None}
#类对象就是类的字典

print(x.__class__)  #<class '__main__.C'> 输出了对象所属的类
print(C.__bases__) #C类父类的元组 (<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__) #<class '__main__.A'> 输出最近的父类

print(C.__mro__) #类的层次结构，从子到父  (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(A.__subclasses__())  #[<class '__main__.C'>]  查看子类的列表

a=20
b=100
c=a.__add__(b) #c=a+b
print(c) #120

class Name():
    def __init__(self,name):
        self.name=name
    def __add__(self, other):  #让两个对象有相加的功能
        return self.name+other.name
    def __len__(self):
        return len(self.name)
name1=Name('zhang')
name2=Name('li')
print(name1+name2)  #zhangli 因为在student类中编写了add()
print(name1.__add__(name2))  #zhangli

lst=[11,22,33]
print(len(lst))
print(lst.__len__()) #3
print(len(name1)) #5
print(len(name2))#2

'''
1、__new__()创建对象
2、__init__()初始化对象
'''
class Human(object):
    def __new__(cls, *args, **kwargs):
        print("__new__被调用了，cls的id值{0}".format(id(cls)))  #类的id，就是Human的id
        obj=super().__new__(cls)
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj
    def __init__(self, name, age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self))) #这里的self就是obj和H1
        self.name = name
        self.age = age

print('object这个类的对象id为{0}'.format(id(object)))
print('Human这个类对象的id为{0}'.format(id(Human)))

H1=Human('张三',20)
#先执行new，将human给new中cls,创建对象obj,在给init中self,最后赋值给H1，所以obj,self和H1中的id是一样的
#先new方法，在初始化init
print('H1这个实例对象的id为{0}'.format(id(H1)))


'''类的赋值和浅拷贝'''
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu1=CPU()  #内存里只有一个对象，但赋值给了两个变量
cpu2=cpu1
print(cpu1)
print(cpu2)  #上下两个是一样的

#类的浅拷贝
disk=Disk()
computer=Computer(cpu1,disk)
import copy
computer2=copy.copy(computer)  #cpu和disk分配的空间一样，子对象不拷贝(所以id一样)，主对象拷贝(所以不一样)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
#<__main__.Computer object at 0x000001E9AF181240> <__main__.CPU object at 0x000001E9AF181198> <__main__.Disk object at 0x000001E9AF181208>
#<__main__.Computer object at 0x000001E9AF181278> <__main__.CPU object at 0x000001E9AF181198> <__main__.Disk object at 0x000001E9AF181208>

#类的深拷贝
computer3=copy.deepcopy(computer)  #子对象和主对象都不一眼了，子对象disk和cpu都是新的，元对象也是新的
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
#<__main__.Computer object at 0x0000023B151D1240> <__main__.CPU object at 0x0000023B151D1198> <__main__.Disk object at 0x0000023B151D1208>
#<__main__.Computer object at 0x0000023B151D1358> <__main__.CPU object at 0x0000023B151D18D0> <__main__.Disk object at 0x0000023B151DD400>
