# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# print_hi('PyCharm')

# l = []
# for i in range(3):
#     x = int(input('integer:\n'))
#     l.append(x)
# l.sort()
# print(l)

# if __name__ == "__main__1":
#     print(6)
#     print(7)
# print(8)

# item_one = "1"
# item_two = "2"
# item_three = "3"
#
# total = item_one + \
#         item_two + \
#         item_three
# print(total)

# print(r"this is a line with \n")

# str = '123456789'
# print(str)
# print(str[0:-1])
# print(str[2:])
# print(str[1:9:2])
# print((str + "你好") * 2)

# input("\n\n按下 enter 键后退出。")

# import sys; x = 'runoob'; sys.stdout.write(x)

# 不换行输出
# x="a"
# y="b"
# print( x, end=" " )
# print( y, end=" " )

# import sys
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

# counter = 100  # 整型变量
# miles = 1000.0  # 浮点型变量
# name = "runoob"  # 字符串
# print(counter)
# print(miles)
# print(name)

# print('Ru\noob')
# print(r'Ru\noob')

# list = ['abcd', 786, 2.23, 'runoob', 70.2]
# tinylist = [123, 'runoob']
# print(list[1:2])
# print(list+tinylist)

# names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# new_names = [name.lower()for name in names if len(name)>3]
# print(new_names)

# a = {x for x in 'abracadabra' if x == 'a'}
# print(a)

# print(python3)

# a = 60
# b = 13
# c = 0
#
# c = a & b
# print("1 - c 的值为：", c)

# a = 10
# b = 20
#
# if (a and b):
#     print("1 - 变量 a 和 b 都为 true")
# else:
#     print("1 - 变量 a 和 b 有一个不为 true")

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
#
# ### 退出提示
# input("点击 enter 键退出")


# i = 256*256
# print('i 的值为：', i)

# a, b = 0, 1
# while b < 20:
#     print(b)
#     a, b = b, a+b

# import support
# support.print_func("Runoob")

# str = input("请输入：");
# print ("你输入的内容是: ", str)

# !/usr/bin/python3

# class JustCounter:
#     __secretCount = 0  # __私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)


# class Site:
#     def __init__(self, name, url):
#         self.name = name  # public
#         self.__url = url  # private
#
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#
#     def __foo(self):  # 私有方法
#         print('这是私有方法')
#
#     def foo(self):  # 公共方法
#         print('这是公共方法')
#         self.__foo()
#
#
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()  # 正常输出
# x.foo()  # 正常输出
# print(x.name)

# print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))


