'''字符串的驻留机制，仅保留一份相同且不可变字符串的方法，后续就不再开辟新的内存空间
一：驻留机制的几种情况（交互模，就是cmd中才可看见）
1、字符串长度为0或者1
2、符合标识符的字符串
3、字符串只再编译时进行驻留，就是直接指明a=?，而不是运行时
4、[-5,256]之间的整数数字
二：好处
1、避免频繁创建和销毁，拼接和修改字符串影响性能
2、字符串拼接时候建议使用join方法（先计算出字符串长度，拷贝，只new一次对象，效率比“+”高）
'''

a='python'
b="python"
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c)) #python 2205553443816
#这里三个输出都是python 2205553443816，id都一样，a,b,c都指向同一个内存空间

'''字符串常用操作'''
#1、查询操作 find好用
s='hello,hello'
print(s.index('lo')) #3 查询第一次出现位置
print(s.find('lo'))
print(s.rindex('lo')) #9查询最后一次出现位置
print(s.rfind('lo'))
#print(s.index('k')) #ValueError: substring not found，index没有查找元素就会抛出异常
print(s.find('k')) #-1 不存在返回-1

#2、大小写转换
s1='hello,pyton'
a=s1.upper()  #全大写，产生新的对象
print(s,id(s1)) #hello,hello 2021832760368
print(a,id(a)) #HELLO,PYTON 2021832794544

print(s1.lower(),id(s1.lower())) #ello,pyton 1530564125296 全部小写

s2='hello,Python'
print(s2.swapcase()) #大写转小写，小写转大写 HELLO,pYTHON
print(s2.capitalize()) #第一个字符转换为大写，其余小写 Hello,python
print(s2.title()) #每个单词第一个字符大写，其余小写 Hello,Python

#3、字符串对其操作
print(s2.center(20,'*')) #****hello,Python**** 居中对其

print(s2.ljust(20,'*'))  #左对其，默认填充空格  hello,Python********
print(s2.ljust(10))  #小于源字符串长度 10<12，返回原来数组

print(s2.rjust(20,'*'))  #********hello,Python

print(s2.zfill(20))  #00000000hello,Python,右对齐，左侧填充0
print(s2.zfill(10)) #hello,Python
print('-8910'.zfill(10)) #-000008910

#4、字符串分割
s3='hello world python'
lst=s3.split() #自动指定空格为分隔符
print(lst)  #['hello', 'world', 'python']
s4='hello|world|python'
print(s4.split(sep='|')) #['hello', 'world', 'python']
print(s4.split(sep='|',maxsplit=1))  #['hello', 'world|python'],只用分出第一段就可以了

print(s3.rsplit())  #['hello', 'world', 'python'] 从右边分割
print(s4.rsplit(sep='|',maxsplit=1)) #['hello|world', 'python'],从右边分割

#5、字符串判断的方法
#1）判断合法标识符
s5='hello,python'
print('1.',s5.isidentifier())  #False, 因为‘，’逗号不是合法的标识符 判断合法标识符
print('2.','张三_123'.isidentifier()) #True

print('3.','\t'.isspace()) #是否为空白字符串

print('4.','abc'.isalpha()) #是否全是字母
print('5.','张三'.isalpha()) #True

print('6.','123'.isdecimal()) #是否全是十进制数字 True，罗马数字不是，四也不是

print('7.','123'.isnumeric()) #是否全是数字
print('8.','123四'.isnumeric()) #True 罗马数字也是数字

print('9.','123as'.isalnum()) #是否全时字母和数字组成
print('10.','张三as'.isalnum()) #True

#6、字符串的替换
s6='hello,Python'
print(s6.replace('Python','Java')) #hello,Java
s7='hello,Python,Python,Python'
print(s7.replace('Python','Java',2)) #hello,Java,Java,Python, 只用替换两个

lst7=['hello','java','python'] #列表
print('|'.join(lst7)) #hello|java|python
print(''.join(lst7)) #hellojavapython

t7=('hello','java','python') #元组
print(''.join(t7))

print('*'.join('python')) #p*y*t*h*o*n

#7、字符串的比较
print('apple'>'app') #True
print('apple'>'banana') #False
print(ord('a'),ord('b')) #97 98
print(chr(97),chr(98)) #a b

'''==与is的区别 ==比较的是value,is比较的是id就是内存第十是否相等'''
a7=b7='python'
c7='python'
print(a7==b7)  #全是true
print(b7==c7)
print(a7 is b7)
print(a7 is c7)

'''字符串的切片操作
1、字符串不可变，不能增删查改
2、切片将产生新的对象
'''
#8、字符串的切片操作
s8='hello,python'
s9=s8[:5] #没有开始，从头开始
print(s9) #hello
s10=s8[6:] #没有结尾，直接到最后
print(s10) #python
s11='!'
newstr=s9+s11+s10
print(newstr) #hello!python
'''完整写法[start:end:step]'''
print(s8[1:5:1]) #从一开始到5，步长为1 ello
print(s8[::2]) #步长2 从开始到最后 hlopto
print(s8[::-1]) #nohtyp,olleh 倒置 步长为复数

#9、格式化字符串
name='张三'
age=20
print('我叫%s,今年%d岁' % (name,age)) #我叫张三,今年20岁

print('我叫{0}，今年{1}岁了，我叫{0}'.format(name,age)) #我叫张三，今年20岁了，我叫张三

#f-string类型格式化字符串
print(f'我叫{name},今年{age}岁') #我叫张三,今年20岁

print('%10d' % 99) #        99 10表示的时宽度
print("%.3f" % 3.1415926) #3.142 保存三位小数
print("%10.3f" % 3.1415926) #     3.142 10为宽度，小数点后三位

print('{0}'.format(3.1415926)) #3.1415926
print('{0:.3}'.format(3.1415926)) #3.14,一共是三位数
print('{0:.3f}'.format(3.1415926)) #3.142,三位小数
print('{0:10.3f}'.format(3.1415926)) #     3.142，同时宽度和精度，10宽度，3精度

#10、字符串的编码转换
s12='天涯共此时'
print(s12.encode(encoding='GBK')) #GBK这种格式中，一个中文占两个字节，b表示2进制
#b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
print(s12.encode(encoding='UTF-8'))  #UTF-8这种格式中，一个中文占三个字节，b表示2进制
#b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'

#解码
#byte代表一个二进制数据（字符类型数据）
byte=s12.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte=s12.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))