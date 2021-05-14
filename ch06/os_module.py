'''os与操作系统相关的模块，可以调用系统文件'''
import os
# os.system('notepad.exe')  #这里像是打开cmd里面的notepad.exe
# os.system('calc.exe')  #打开计算器

#可以直接调用可执行文件
# os.startfile('C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQ.exe')

print(os.getcwd())  #E:\PycharmProjects\study_test\ch06 当前工作路径
lst=os.listdir('../ch05')  #输出ch05中的文件和目录 ['class.py', 'face_object.py']
print(lst)

# os.mkdir('newdir')  #创建新目录
# os.makedirs('A/B/C') #创建多级目录
# os.rmdir('newdir') #删除
# os.removedirs('A/B/C') #删除
# chdir(path),将path设置为当前目录

print(os.path.abspath('os_module.py')) #获得文件或目录的绝对路径
print(os.path.exists('os_module.py')) #判断是否存在该文件 true
# print(os.path.join())  将目录与文件名结合起来
# print(os.path.split()) 将文件路径和文件名分开
print(os.path.splitext('os_module.py')) #('os_module', '.py')
# print(os.path.basename()) 提取文件名字
# dirname()提取目录
# isdir() 判断是否为路径

'''获取指定目录下的所有py文件'''
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

lst_files=os.walk(path)  #得到所有的文件
print(lst_files)
for dirpath,dirname,filename in lst_files:  #先遍历当前目录ch06下的文件，再区遍历子文件名字
    '''
    print(dirpath) #E:\PycharmProjects\study_test\ch06  E:\PycharmProjects\study_test\ch06\bag
    print(dirname) #['bag'] 文件 []
    print(filename) #['a.txt', 'b.txt', 'doc_read_open.py', 'modul.py', 'os_module.py']  ['package.py', '__init__.py']
    '''
    for dir in dirname: #当前目录下有多少个子目录
        print(os.path.join(dirpath,dir)) #E:\PycharmProjects\study_test\ch06\bag
    for file in filename:
        print(os.path.join(dirpath, file))  #得到所有的文件路径，ch06下