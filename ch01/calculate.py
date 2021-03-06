#有关加减乘除
print(1+1)
print(1/2)#除法运算
print(11//2)#整除运算
print(11%2) #取余数运算
print(2**2)#平方运算

#注意一正一复数
print(9/-4)
print(9//-4) #这里为-3，向下取整
print(-9%4) #这里为3  余数=被除数-除数*商 -9-4*(-3)=3
print(9%-4) #这里为-3

#链式赋值
a=b=c=20  #这里a,b,c三个地址id都相同的

#支持参数赋值
a=20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a)
a/=3  #float
a//=2 #float

#解包赋值
a,b,c=20,30,40
print(a,b,c)

#交换变量
a,b=10,20
print("交换之前",a,b)
a,b=b,a
print("交换之后",a,b)

#比较运算符
a,b=10,20
print('a>b吗',a>b) #返回布尔值
a=10
b=10
print(a==b) #value相等
print(a is b) #a与b的id标识相等，此处还有is not
#但列表list，list1=[1,2,3]列表如果相同，id是不同的

#布尔运算符就是指and 和 or,not,in,not in
s='hello'
print('w' in s)

#关于每个位的运算
print(4&8) #这里是按位与，就是100与1000相与就是0
print(4|8) #按照位置或运算，这里是12
print(4<<1) #左移位，这里高位溢出，地位就可以补0，向左一位，乘以2
print(4>>2) #右移位，就是除以二，高位补充0 向右移动两位

#python中算数的运算优先级
'''
**, *,/,//,%, +,-,(算数运算)
>>,<<
&, 与
|,或
>,<,=,==,!=,<=
and,
or,
=.
算数，位，比较，布尔，赋值，括号优先级最高
'''