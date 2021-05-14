'''关于模块
注意如果自定义模块有问题，可以右击目录ch06，选择标记目录为，源码根
python解释器内部使用Unicode
外部.py使用utf-8  不同编码格式决定磁盘占用大小 gbk和utf-8
'''
#encoding=utf-8
import math
from math import pi #这里就可以直接使用pi,不用math.pi了
import bag.package as m  #导入自己写的包里的module,包.模块名称
from bag import package as m #用from可以导入函数，变量，模块
print(m.a)


if __name__=='__main__':  #表示以主程序方式运行才可以运行里面的内容，被其他包应用就不会
    print(id(math))
    print((type(math)))  # <class 'module'>
    print(math)  # <module 'math' (built-in)> build-in表示自带的
    print(math.pi)  # Π
    print(pi)  # Π
    print(dir(math))  # 可以知道所有的方法

