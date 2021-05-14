'''
关于类，python中一切皆是对象，对象表示有id,type是否开辟内存空间
类里面定义的叫方法
类外定义的叫函数
'''

class Student: #要求类名中每个单词的首字母大写，其余小写，可由一个或多个单词组成
     native_place='陕西' #直接写在类里面的变量称为类属性

     def __init__(self,name,age):
         self.name=name  #self.name是实例属性，将局部变量name赋值给实例属性
         self.age=age

     def eat(self): #实例方法
         print('Students ar eating now...')
         print(self.name+'在吃饭')

     @staticmethod  #这里表示静态方法
     def method():  #不需要使用self
         print('这里是静态方法')

     @classmethod  #这里是类方法
     def cm(cls): #cls传递类
         print('这里是类方法')

print(id(Student)) #类对象
print(type(Student))

#创建对象
stu1=Student('张三',20) #实例对象传实例对象self
print(id(stu1))
print(type(stu1))
stu1.eat() #对象名.方法名（）
Student.eat(stu1) #这个与上面方法相同，stu1=self，类名.方法名（类对象）
print(stu1.name)

#这里是类属性
print(Student.native_place)
print(stu1.native_place)

Student.native_place='天津'
print(stu1.native_place) #天津

#类方法使用方式
Student.cm()  #这里是类方法,直接使用类名调用

#静态方法使用
Student.method() #这里是静态方法,直接使用类名调用

#动态绑定
stu1=Student('张三',20)
stu1.gender='女'  #这里就是动态绑定，只给stu1一个属性gender
stu2=Student('李四',20)
# print(stu2.gender)  不存在这个属性

def show(): #函数方法，绑定在stu1上面
    print('和stu1绑定')
stu1.show=show
stu1.show()
# stu2.show()  这个就是错误的

with Student() as Stu:
    Stu.eat()




