print(520)
print('Helloworld')
print("hello")
print(3+1)  #4


#数据输出到文件中：使用file=fp的形式
fp=open('D:/text.txt','a+')  #a+表示如果文件不存在就创建，如果存在就在文件内容后面追加
print('helloworld',file=fp)
fp.close()

#不进行换行输出：
print('hello','world','python')

#转义字符
print('hello\nworld') #\n表示换行，newline
print('hello\tworld') #\t 表示tab,每次个为一个tab
print('hello\rworld') #表示return，会覆盖掉前面的
print('hello\bworld') #表示退一格 backspace

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

#原字符，不希望字符串中国转义字符有作用，在字符串前加上r/R
print(r'hello\nworld')

#字符转换
print(chr(0b0100111001011000)) #乘
print(ord('乘')) #20056


#值,注意多次赋值后会造成内存垃圾
name="周"
print('标识',id(name))  #id
print('类型',type(name))  #type
print('值',name) #value

#数据类型转换
name='张三'
age=20  #int转换为str
print('我叫'+name+'今年，'+str(age)+'岁')

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

