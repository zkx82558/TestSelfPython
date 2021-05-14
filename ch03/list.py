#有关列表
lst=['hello','python',10]  #相当于整个list是一个id，但其实列表中的每个对象其实也是对象也有id
print(id(lst))
print(type(lst))
print(lst)

#列表创建
lst2=list(['hello','python',98])
#存储的是一个内存的使用，创建三个连续空间列表对象

#列表特点
'''
不同的数据类型可以混合存储
'''

#获得列表索引
lst3=list(['hello','python',98,'hello'])
print(lst3.index('hello')) #如果列表中有相同元素，只返回第一个出现元素的索引，这里是0
print(lst3.index('hello',2,4)) #这里指在索引1和4-1=3之间找hello的索引
print(lst3[2])
print(lst3[-1]) #-1就是指倒数第一个元素

#list切片
lst4=[10,20,30,40,50,60,70,80,90]
print(lst4[1:6:1]) #这里表示开始是1，结尾是6，步长为一截取list,截取出来的还是数组list
lst5=lst4[1:6:1] #不写步长，那默认也为1，省略start也是从0，stop省略就是直接到最后
#step为复数的情况
print(lst4[::-1]) #逆序输出，这里第一个元素是原来列表的最后一个，最后一个是第一个
#[90, 80, 70, 60, 50, 40, 30, 20, 10]
print(lst4[6:0:-2]) #[70, 50, 30]

#列表元素遍历和循环
lst5=[10,20,'python','hello']
print(10 in lst5) #True
print(100 not in lst5)
for item in lst5:
    print(item)

#列表元素的增删改
lst6=[10,20,30,40]
lst6.append(100) #向列表后面添加100
lst7=['hello','world']
#增加
lst6.append(lst7)
print(lst6) #[10, 20, 30, 40, 100, ['hello', 'world']]
lst6.extend(lst7)
print(lst6) #[10, 20, 30, 40, 100, 'hello', 'world']
lst6.insert(1,90) #在索引1处添加90
lst6[1:]=lst7
print(lst6) #[10, 'hello', 'world']直接切片，将1后面的改为lst7

#删除
lst8=[10,20,30,40,50,30]
lst8.remove(30) #移除的是重复元素的第一个元素,移除30这个数字
print(lst8)
lst8.pop(1) #移除索引为1的数字，如果不指定参数，将删除列表中最后一个元素
print(lst8)
#如果用切片元素的化，会得到一个新的列表对象
#如果想要不产生新的列表对象，而是删除
lst8[1:3]=[]
print(lst8)
lst.clear() #清除列表
del lst #表示删除list

#更改列表
lst9=[10,20,30,40]
lst9[2]=100
print(lst9) #更改
lst9[1:3]=[300,400,500,600] #[10, 300, 400, 500, 600, 40]
print(lst9)

#列表的排序 sort() reverse=true 降序
lst10=[20,40,50,70,100,54,3]
lst10.sort() #升序排序 [3, 20, 40, 50, 54, 70, 100]
print(lst10)
lst10.sort(reverse=True) #[100, 70, 54, 50, 40, 20, 3]降序
print(lst10)
new_lst10=sorted(lst10) #升序，产生新的对象 sorted(lst10,reverse=Ture)降序
print(new_lst10)

#列表生产式
lst11=[i for i in range(1,10)]
print(lst11)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
lst11=[i*i for i in range(1,11)]
print(lst11)