def calc(a,b):
    c=a+b
    return c

result=calc(20,10)
print(result)
res=calc(b=10,a=20) #按照里面的定义传递
print(res)

'''如果是不可变对象，函数体内修改不会修改实参的值
如果可变，函数内修改会改变实参的值
'''

'''
函数的返回值
1）如果函数不需要返回值，可以不写return
2）函数的返回值如果是1个，那就直接返回原本类型的值
3）如果函数返回值有多个，那么返回的结果为元组
'''
def fun1():
    print('hello')

def fun2():
    return('hello')
res2=fun2()

def fun3():
    return 'hello','world'
print(fun3()) #('hello', 'world')

'''
函数定义时候，如果形参有默认值，只有与默认值不一样时候才需要重新传递
'''
def fun4(a,b=10):
    print(a,b)
fun4(100) #100 10
fun4(29,90) #29 90
print('hello',end='\t')
print('world')  #hello	world

'''个数可变的位置参数只能一个，当不知道传递的位置实参有多少个的时候，*?,结果为一个元组,可以写多个'''
def fun5(*args):
    print(args)
    print(args[0])

fun5(200) #(200,) 都是元组
fun5(200,300400)  #(200, 300400)

'''个数可变的关键字参数只能一个，当无法确定传递的关键字实参的个数时，使用可变的关键字形参，**args,结果为一个字典'''
def fun6(**args):
    print(args)

fun6(a=10) #{'a': 10}
fun6(a=20,c=40,n=100) #{'a': 20, 'c': 40, 'n': 100}

def fun7(*args,**args2): #可存在位置参数，也可存在关键数参数，位置参数要放在前面
    pass


def fun8(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
fun8(10,20,30)
lst=[11,22,33]
fun8(*lst) #在函数调用时，将列表中每个元素都转换为位置参数传入

fun8(a=10,b=20,c=90) #关键词传参
dic={'a':111,'b':222,'c':333}
fun8(**dic) #将字典中的键值对转换为关键字参数传入


def fun9(a,b,*,c): #这里表示c只能使用关键字实参传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
fun9(10,20,c=30)

def fun10(a,b,*,c,d,**args):
    pass
def fun11(*args,**args2):
    pass
def fun12(a,b=10,*args,**args2):
    pass

'''
函数体内的变量为局部变量，函数外使用就是超出了作用域
函数外定义，是全局变量，函数内部外部都可以使用
如果在函数体内声明 golbal age,那么age这个参数再外面也可以使用
'''

'''递归函数：占用内存，效率低下，思路简单'''
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6)) #720,这里是6的阶乘

'''斐波那契数列（1，1，2，3，5，8，13），就是第三项是前两项的和'''
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))
for i in range(1,7):
    print(fib(i))