'''
try:

except 加捕获的异常情况： (先捕获子类，就是小的)
except 加捕获的异常情况： (在捕获父类，就是大的)
  (有异常的时候执行except中)
else:
 (没有异常后就执行else中的)
finally:

'''

try:
    a1=int(input('请输入一个整数'))
    a2 = int(input('请输入另一个整数'))
    result=a1/a2
except BaseException as e: #包括还有valueError等等异常。这里的BaseException表示所有的异常情况
    print('出错了',e)
else:
    print('计算结果为：',result)
finally:
    print('无论是否产生异常都会执行')
print('程序结束')

'''
1、ZeroDivisionError 10/0
2、IndexError 索引错误
3、KeyError  字典键值错误
4、NameError 没有声明变量
5、SyntaxError 语法错误
6、ValueError 传入无效参数
'''

'''Tracsback,打印异常信息'''
import traceback
try:
    print('------------------------')
    print(1/0)
except:
    traceback.print_exc()