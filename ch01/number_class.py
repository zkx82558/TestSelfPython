#关于数据，整数
n1=90
n2=-90
print(n1,type(n1))
#整数中可以表示为十进制、二进制等等
#数据前加上0b可以将二进制变为十进制，0o八进制转为十进制，0x将十六进制变为十进制

#浮点类型
a=3.1415
print(a,type(a))
print(1.1+2.2) #3.3000000000000003
#注意存储浮点数计算会有问题，所以要导入模块
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2')) #3.3

#布尔类型boolean
f1=True #1
f2=False #0
print(f1+1)
print(f2+1)

#字符串类型
#''' '''可以在多行显示
str1='好难啊！' #或可以用""
str2='''好难，
加油''' #或者""" """
print(str2,type(str2))
print(str1,type(str1))

#数据类型转换
name='张三'
age=20  #int转换为str
print('我叫'+name+'今年，'+str(age)+'岁')

#将其他转换为str类型 str()
a=10
b=189.11
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c))

#转换为int,str的字符串要为数字才可以  int()
s1='190' #string
s2=90.17 #转换后变为90
s3='90.17' #不可以转换,小数不可以
s4=True #转换为1
s5="hello" #不可以转换
print(int(s1),type(int(s1)))

#float(),浮点数的转换
f1='190.01' #可以转换
f2='90' #转换为90.0
f3=True #转化为1.0
f4='hello' #不可以转换，内部要为数字才可以
f5=90 #可以转换


#注意这里有编码格式可以改变 比如加上#coding:gbk/utf-8 写在文件最前面
