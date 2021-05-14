'''
元组是不可变序列
不可变序列：整数，字符串，元组（不可以进行增删查改）
可变序列：列表，字典（可以增删查改，对象地址，内存地址不改变）
元组是没有生成式的应为他不可变
'''

s='hello'
s=s+'world'
print(s)
#这里前后的s的id不一样，实际上内存地址改变

#元组创建方式
t=('python','world',98)
print(t)
print(type(t))

t1=tuple(('python','world',98)) #tuple()内置函数，里面再加（）表示元组
print(t1)
print(type(t1))

t2='python','world',98
print(t2)
print(type(t2))
#('python', 'world', 98)
#<class 'tuple'>

t3=('python',) #如果元组中只有一个元素，就不可以省略,
#空元组创建
t4=()
t5=tuple()

'''
元组为不可变序列，多任务环境下，同时操作对象时不需要加锁，故要使用,如果多人使用，这时候第一个使用的人加锁
1）如果元组对象本身为不可变对象，则不能引用其他对象，
2）如果元组对象是可变对象，则可变对象的引用不允许改变，但数据可改变
比如元组里面有list，不能把list变成其他数，但可以改变list里面的数字
'''

t7=(10,[20,30],9)
print(t7)
print(type(t7))
print(t7[0],type(t7[0]),id(t7[0])) #10 <class 'int'> 1475505472
print(t7[1],type(t7[1]),id(t7[1])) #[20, 30] <class 'list'> 1422705990728
print(t7[2],type(t7[2]),id(t7[2])) #9 <class 'int'> 1475505440

#t7[1]=100 #TypeError: 'tuple' object does not support item assignment，这时候报错

t7[1].append(100) #列表中的元素可以改变
print(t7,type(t7[1]),id(t7[1]))  #(10, [20, 30, 100], 9) <class 'list'> 1692759530568

t8=tuple(('python','world',98))
for items in t8:
    print(items)