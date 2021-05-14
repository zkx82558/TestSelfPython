'''
总结：
1、列表list()   可变    可重复    有序  []
2、元组tuple()  不可变  可重复    无序  （）   元组遍历for in，没有增删查改
3、字典dict()   可变    key不可变 value可变  无序  {key:value}  浪费内存，但查得快
4、集合set()    可变    不可重复  无序  {}     增加：add().update()删除：remove().discard().pop().clear()
'''

'''
1、python提供的内置数据结构
2、与列表字典一样是可变序列，但没有value
3、同样根据依据哈希函数进行位置存储，无序列，与字典一样
'''

#集合的建立
s={2,3,4,5,5,6,7,7}
print(s) #{2, 3, 4, 5, 6, 7} 集合中元素不允许重复

s1=set(range(6))
print(s1,type(s1))  #{0, 1, 2, 3, 4, 5} <class 'set'>

s2=set([1,2,3,4,4,5,5,5])
print(s2,type(s2))  #{1, 2, 3, 4, 5} <class 'set'> 将列表转换为集合

s3=set((1,2,3,3,4,65))
print(s3,type(s3))  #{65, 1, 2, 3, 4} <class 'set'> 集合中的元素无序，最后一个65却到了最前面

s4=set('python')
print(s4,type(s4)) #{'p', 'n', 't', 'o', 'h', 'y'} <class 'set'> 无序

s5=set({1,2,3,4,5,5}) #{}本身定义的就是集合类型
print(s5,type(s5))  #{1, 2, 3, 4, 5} <class 'set'>

s6={}
print(type(s6))  #<class 'dict'> 这样是字典

s7=set()
print(type(s7))  #<class 'set'>

'''集合的相关操作'''
#1、判断操作
s8={1,2,3,3,4,4}
print(1 in s8) #True or not in
#2、添加操作
'''add一次添加一个，update可以添加多个元素比如：集合，元组，列表等'''
s8.add(80)
print(s8) #{1, 2, 3, 4, 80}
s8.update({200,400,300}) #放入集合
print(s8) #{1, 2, 3, 4, 200, 300, 80, 400}
s8.update([100,90])
print(s8) #{1, 2, 3, 4, 100, 200, 300, 80, 400, 90}
s8.update((78,90,100))
print(s8) #{1, 2, 3, 4, 100, 200, 300, 78, 80, 400, 90}

#3、删除
''' discard好用'''
s8.remove(100)  #如果没有该元素，就会抛出异常,kryerror
print(s8)
s8.discard(90000) #元素不存在，不会抛出异常
print(s8)
s8.pop()
print(s8)  #{2, 3, 4, 200, 300, 78, 80, 400, 90},此处自动删除哈希函数后第一个值,pop()内部不能有参数
s8.clear()
print(s8) #set()清空所有元素

'''集合的关系'''
s9={10,20,30,40}
s10={20,30,10,40}
print(s9==s10)  #True 集合无序，所以是true,元素相等
'''子集'''
s11={10,20,30,40,50,60}
s12={10,20,30,40}
s13={10,20}
print(s12.issubset(s11))  #判断是否为子集
print(s13.issubset(s12))  #True
'''超集，B是A的子集，A是B的超集'''
print(s11.issuperset(s12))  #判断为超集
print(s12.issuperset(s13))
'''两个集合是否有交集'''
print(s12.isdisjoint(s13)) #False,有交集为False
#没有交集是True

'''集合的数学操作'''
#1、求交集
print(s11.intersection(s12))  #{40, 10, 20, 30}
print(s11 & s12) #{40, 10, 20, 30}
#2、求并集
print(s11.union(s12)) #{40, 10, 50, 20, 60, 30}
print(s11|s12)  #{40, 10, 50, 20, 60, 30}
#3、差集操作，就是减法
print(s11.difference(s12)) #{50, 60} s11-s12，减去s12中与s11中相同元素，留下的是s11中元素
print(s11-s12)
#4、对称差集
print(s11.symmetric_difference(s12)) #{50, 60}相减，留下的是s11和s12中的元素
print(s11^s12)

'''集合生成式子，元组是没有生成式的应为他不可变'''
#列表生成
lst=[i*i for i in range(6)]
#集合生成
s14={i*i for i in range(10)}
print(s14) #{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}



