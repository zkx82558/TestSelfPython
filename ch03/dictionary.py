'''
字典 {} 以键值对的方式存储 ，键要是不可变序列，可变序列，
hash(key)经过哈希处理后才进行排列，这样顺序就是固定的，先计算哈希函数，找到key位置取出value值
字典内存浪费较大，但查询速度快
列表是有序的，可变序列
'''

#字典的创建方式 dict
sources={'张三':100,'李四':400}
student=dict(name='jack',age=100)
d={} #空字典

#查找
print(sources['张三']) #如果没有，就会报错
print(sources.get('张三')) #如果查找的键没有就是输出None
print(sources.get('马奇',99)) #没有马奇，就会返回99这个值  99

#删除
print('张三' in sources) #True 或not in
del sources['张三'] #删除指定键值对 {'李四': 400}
print(sources)
#sources.clear() #清除字典中所有元素

#增加和改变
sources['陈六']=98 #{'李四': 400, '陈六': 98},修改元素直接修改就可以=？
print(sources)

#获取字典视图
keys=sources.keys()
print(keys) #dict_keys(['李四', '陈六'])
print(type(keys)) #<class 'dict_keys'>
print(list(keys)) #['李四', '陈六'] 将键值对转换成列表

values=sources.values()
print(values) #dict_values([400, 98])
print(type(values)) #<class 'dict_values'>

items=sources.items()
print(items) #dict_items([('李四', 400), ('陈六', 98)]) 每一个元素是一个元组
print(type(items)) #<class 'dict_items'>
print(list(items)) #[('李四', 400), ('陈六', 98)]

#字典元素的遍历
for item in sources:  #这里遍历出来的是键，不是value
    print(item,sources[item],sources.get(item))
    #李四 400 400
    #陈六 98 98

#zip()打包字典生产式
sour=['fruit','book','others']
prices=[98,97,10]
d={item.upper():price for item,price in zip(sour,prices)}
print(d) #{'FRUIT': 98, 'BOOK': 97, 'OTHERS': 10}
#如果是字典打包{}不是[]，那就是乱序，如果打包数字不一样，以少一点的为准
