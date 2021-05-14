'''关于文件的读取'''
file=open('a.txt','r',encoding='utf-8',errors='ignore')
file.seek(2) #一个中文占据两个字节，跳过第一个字
print(file.readlines())
# print(file.read())
file.tell() #就是把光标移动到最后面，直接跳到最后
file.close()

'''使用with语句可以不用关闭文件'''
with open('a.txt','r',encoding='utf-8',errors='ignore') as file:
    print(file.read())
#相当于with语句先调用enter,再函数，在exit，就是自动退出


file=open('b.txt','w') #写入，每次重新写入
# file.write('helloworld')
lst=['java','go','python']
file.writelines(lst)
file.flush() #缓冲，后面可以继续写内容
file.write('hello')
file.close()


# file=open('b.txt','a')  #一直写入，没有就写入，有就继续写  a+就是指读写的方式
# file.write('python')
# file.close()

#复制图片功能 rb是二进制
'''
src_file=open('one.png','rb')
target_file=open('two.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()

with open('one.png','rb') as src_file:
    with open('two.png','wb') as target_file
        target_file.write(src_file.read())s
'''
