#这里主要是循环

#range()函数
r=range(10)
print(r)  #range(0, 10)
print(list(r))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],表示列表
r1=range(3,10) #开始和结束，未指定步长
r2=range(1,10,2) #在给定步长,[1, 3, 5, 7, 9]
print(list(r2))
print(9 in r2)
print(list(range(1,20,2)))  #只有用到range中时候，才会使用到他有这里面的对象

#循环结构
a=1
while a<10:
    print(a)
    a+=1

b=1
sum=0
while b<=100:
    if b%2==0:  #这里变为b%2,如果为0，就是偶数但0的布尔值为false/或者 if not bool()
        sum+=b
    b+=1
print('100之内的偶数和：',sum)

#for循环
for item in 'python':
    print(item)
#可以用range()产生整数序列
for i in range(10):
    print(i)  #产生0到9
#如果在循环体中无需自定义变量，则可以写为_
for _ in range(3): #range(1,100)
    print("好烦哦")

'''
break,非正常结束循环，if,就跳出循环
continue,就是表示结束此次的循环，然后到下一次循环
else还有一个是整个循环执行完毕的最后一次执行else里面的函数
for  :
else
while:
else
'''

