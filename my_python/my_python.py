# # 1-Hello world!
# print("Hello world!")

# # 2-python之禅
# import this

# # 4-画正方形
# import turtle
#
# turtle.pensize(4)
# turtle.pencolor('red')
#
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
#
# turtle.mainloop()


# # 6-运算符
# # 6.1-提示：华氏温度到摄氏温度的转换公式为：C=(F−32)÷1.8
# print("Please input the F:")
# F = float(input())
# C = (F-32)/1.8
# # print("The C is: %.1f." % C)
# # print("The C is: {:.1f}".format(C))
# print(f'The C is: {C:.1f}')

# # 7-输入圆的半径计算计算周长和面积。
# # c = 2*pi*r
# # s = pi*r*r
# import math
#
# r = float(input("Please input the r:"))
# c = 2 * math.pi * r
# s = math.pi * r * r
# print("The c is: %.1f" % c)
# print(f'The s is: {s:.1f}')

# # 8-分支结构：if/else
# # 判断闰年
# # 1、能被4整除，但不能被100整除；
# # 2、能被400整除；
# print("Please input the year:")
# year = int(input())
# is_leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
# if is_leap:
#     print("这是闰年！")
# else:
#     print("这不是闰年！")


# # 9-英制单位英寸与公制单位厘米互换。
# # 1英寸=2.54厘米
# value = float(input("请输入长度："))
# unit = input("请输入单位：")
# if unit == "in" or unit == "英寸":
#     print("%f 英寸 == %f 厘米" % (value, value*2.54))
# elif unit == "cm" or unit == "厘米":
#     print("%f 厘米 == %f 英寸" % (value, value/2.54))
# else:
#     print("请输入正确的单位！")


# # 10-百分制成绩转换为等级制成绩。
# # 要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
# 问题：如果输入是字符或者其他异常输入呢？
# score = float(input("请输入成绩："))
# if score >= 90:
#     # print("成绩为A")
#     grade = 'A'
# elif (score >= 80) and (score < 90):
#     # print("成绩为B")
#     grade = 'B'
# elif (score >= 70) and (score < 80):
#     # print("成绩为C")
#     grade = 'C'
# elif (score >= 60) and (score < 70):
#     # print("成绩为D")
#     grade = 'D'
# # elif score < 60:
# #     # print("成绩为E")
# else:
#     # print("请输入正确的成绩！")
#     grade = 'E'
#
# print(f'您的成绩为{grade}!')


# # 11-输入三条边长，如果能构成三角形就计算周长和面积。
# # 三角形：两边之和大于第三边
# # 周长：三边相加
# # 面积：海伦公式
# print("请输入三条边长：")
# a = float(input("第一条边："))
# b = float(input("第二条边："))
# c = float(input("第三条边："))
# z = a + b + c
# p = z / 2
# s = (p * (p-a) * (p-b) * (p-c)) ** 0.5
#
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("这三条边能构成三角形")
#     print(f'这个三角形的周长是{z}，面积是{s}。')
# else:
#     print("这三条边不能构成三角形。")


# #  12-用for循环实现1~100之间的偶数求和
# sum1 = 0
# for x in range(2, 101, 2):
#     sum1 += x
# print(sum1)


# # 13-循环结构：for-in循环，while循环
# # break关键字，它的作用是提前结束循环。需要注意的是，break只能终止它所在的那个循环，这一点在使用嵌套循环结构时需要引起注意。
# 另一个关键字是continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。
# # 13.1-输入一个正整数判断是不是素数。
# # 提示：素数指的是只能被1和自身整除的大于1的整数。
# # 算法一:针对输入的数字x，我们可以遍历从2到x-1这个区间中的数，如果x能被这个区间中任意一个数整除，那么它就不是质数。
# # 算法二：对算法一的优化，事实上只需要遍历从2到√x即可。
# # 其他算法参考网络
# from math import sqrt
#
# num = int(input("请输入一个正整数："))
# is_prime = True
# # # 算法一：
# # for i in range(2, num):
# #     if num % i == 0:
# #         is_prime = False
# #         break
# # if is_prime and num > 1:
# #     print(f'{num}是素数')
# # else:
# #     print("%d不是素数" % num)
# # 算法二：
# end = int(sqrt(num))
# for i in range(2, end+1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num > 1:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')


# # 14-输入两个正整数，计算它们的最大公约数和最小公倍数。
# # 两个数的最大公约数common divisor是两个数的公共因子中最大的那个数；两个数的最小公倍数common multiple则是能够同时被两个数整除的最小的那个数。
# # 两个自然数的乘积等于这两个自然数的最大公约数和最小公倍数的乘积。
# x = int(input("请输入正整数x："))
# y = int(input("请输入正整数y："))
# if x > y:
#     x, y = y, x
# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(f'{x}和{y}的最大公约数是：{i}')
#         print(f'{x}和{y}的最小公倍数是：{int((x*y)/i)}')
#         break


# # 15-打印如下所示的三角形图案。
# row = int(input("请输入行数："))
# # for i in range(row):
# #     print(i)
#
# for i in range(row):
#     # for _ in range(n) 一般仅仅用于循环n次，不用设置变量，用 _ 指代临时变量，只在这个语句中使用一次。
#     for _ in range(i + 1):
#         # end的作用就是告诉print，将print自带的换行用end中指定的str代替
#         print('*', end='')
#     # 打印完*之后恢复换行
#     print()
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

# # 16-寻找水仙花数。
# # 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：1^3 + 5^3+ 3^3=153
# # %：取模 - 返回除法的余数;
# # //：取整除 - 返回商的整数部分(向下取整）;
# # **：幂 - 返回x的y次幂
# # 利用//和%拆分一个数的小技巧在写代码的时候还是很常用的
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100 % 10
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(f'{num}是水仙数。')

# # 17-正整数的反转，例如将12345变成54321
# # 利用//和%拆分一个数
# num = int(input("Please input a number:"))
# re_num = 0
# while num > 0:
#     re_num = re_num * 10 + num % 10
#     num = num // 10
# print(re_num)

# # 18-百钱百鸡问题.
# # 说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# # 翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
# # 假设公鸡的数量为x，x的取值范围是0到20；母鸡的数量为y，y的取值范围是0到33；小鸡的数量为z，z=100-x-y
# for x in range(0, 21):
#     for y in range(0, 34):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(f'公鸡：{x}只，母鸡：{y}只，小鸡：{z}只')

# 19-CRAPS赌博游戏
# CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。

# 20-斐波那契数列
# 斐波那契数列（Fibonacci sequence），通常也被称作黄金分割数列，
# 是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中研究在理想假设条件下兔子成长率问题而引入的数列，因此这个数列也常被戏称为“兔子数列”。
# 斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，按照这个规律，斐波那契数列的前10个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55。
# 斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

# 21-打印100以内的素数。
# 素数指的是只能被1和自身整除的正整数（不包括1）。

# # 22-将一颗色子掷6000次，统计每个点数出现的次数
# # 方法：用counters列表中的六个元素分别表示1到6的点数出现的次数，最开始的时候六个元素的值都是0。接下来用随机数模拟掷色子，如果摇出1点counters[0]的值加1，如果摇出2点counters[1]的值加1，以此类推
# import random
# counters = [0] * 6
# for _ in range(6000):
#     face = random.randint(1, 6)
#     counters[face - 1] += 1
# for face in range(1,7):
#     print(f'{face}点出现了{counters[face -1]}次！')


# 23-容器型数据类型：列表list，元组tuple，字符串str，集合set，字典dict
# 列表：list，[]。列表是容器，可以保存各种类型的数据，可以通过索引操作列表元素
# 元组：tuple，()。有几个元素称为几元组。
# 字符串：string，''或者""。
# 集合：set,{}，需要至少有一个元素，没有元素就是空字典,空集合set();。容器型数据类型。集合底层使用了哈希存储的方式，元素必须是hashable类型，与列表不同的地方在于集合中的元素没有序、不能用索引运算、不能重复。
# 字典：dict,{key:value}
# 列表和元组都是容器型的数据类型，即一个变量可以保存多个数据。列表是可变数据类型，元组是不可变数据类型，所以列表添加元素、删除元素、清空、排序等方法对于元组来说是不成立的。但是列表和元组都可以进行拼接、成员运算、索引和切片这些操作。字符串类型也是这样，因为字符串就是字符按一定顺序构成的序列，在这一点上三者并没有什么区别。
# 我们推荐大家使用列表的生成式语法来创建列表，它很好用，也是Python中非常有特色的语法。

# # 23.1-列表的生成式：强烈建议用生成式语法来创建列表
# # 创建一个由1到9的数字构成的列表
# items1 = [x for x in range(1, 10)]
# print(items1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
# items2 = [x for x in 'hello world' if x not in ' aeiou']
# print(items2)    # ['h', 'l', 'l', 'w', 'r', 'l', 'd']
#
# # 创建一个由个两个字符串中字符的笛卡尔积构成的列表
# items3 = [x + y for x in 'ABC' for y in '12']
# print(items3)    # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

# # 23.2-字符串相关。转义字符，用反斜杠 \ 转义字符
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)
# print(a)
# print("\n")
# print(a)
# print(r'\n')  # r/R:非转义的原始字符串
# print(b'\n')
# print(b'a')  # b:bytes，打印以b开头。python3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes，
# print(f'print format string " {a} "')  # f或者format()，格式化操作
# print(u'Hello\u0020World !')  # u/U:表示unicode字符串,被替换的 \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）
# # 一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。建议所有编码方式采用utf8

# # 23.3-占位符
# name = 'Li hua'
# age = 24
# print("加号拼接字符串：" + "Hello " + name + ", you are " + str(age) + " years old.")
# print(r"%占位符：" + "Hello %s, you are %d years old." % (name, age))
# print("format占位符：Hello {name}, you are {age} years old.".format(name='Li hua', age=24))
# print("format占位符：Hello {}, you are {} years old.".format('Li hua', 24))
# print("f表达式：" + f'Hello {name}, you are {age} years old.')

# # 24-dict函数(构造器)中的每一组参数就是字典中的一组键值对
# person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号')
# print(person)    # {'name': '王大锤', 'age': 55, 'weight': 60, 'home': '中同仁路8号'}
#
# # 可以通过Python内置函数zip压缩两个序列并创建字典
# items1 = dict(zip('ABCDE', '12345'))
# print(items1)    # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
# items2 = dict(zip('ABCDE', range(1, 10)))
# print(items2)    # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
#
# # 用字典生成式语法创建字典
# items3 = {x: x ** 3 for x in range(1, 6)}
# print(items3)     # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# # 25-输入一段话，统计每个英文字母出现的次数。
# sentence = input('请输入一句话：')
# counter = {}
# for ch in sentence:
#     if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
#         counter[ch] = counter.get(ch,0) + 1
# for k, v in counter.items():
#     print(f'字母{k}出现了{v}次。')

# 26-在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
# 说明：可以用字典的生成式语法来创建这个新字典。
# stocks = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# s2 = {k: v for k, v in stocks.items() if v > 100}
# print(s2)

# # 27-设计一个生成验证码的函数。
# # 说明：验证码由数字和英文大小写字母构成，长度可以用参数指定。
# 说明：random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样，这意味着抽样取出的字符是不重复的；choices实现有放回抽样，这意味着可能会重复选中某些字符。这两个函数的第一个参数代表抽样的总体，而参数k代表抽样的数量。
# import random
# import string
#
# strings = string.digits + string.ascii_letters
#
#
# def generate_code(code_len=4):
#     code = ''.join(random.choices(strings, k=code_len))
#     # code = random.choices(strings, k=code_len) # 打印出来是列表，需要用join连接起来
#     # print(code)
#     return code
#
#
# if __name__ == '__main__':
#     for _ in range(10):
#         print(generate_code())

# # 28-设计一个函数返回给定文件的后缀名。
# # 说明：文件名通常是一个字符串，而文件的后缀名指的是文件名中最后一个.后面的部分，也称为文件的扩展名，它是某些操作系统用来标记文件类型的一种机制，
# 例如在Windows系统上，后缀名exe表示这是一个可执行程序，而后缀名txt表示这是一个纯文本文件。
# # 需要注意的是，在Linux和macOS系统上，文件名可以以.开头，表示这是一个隐藏文件，像.gitignore这样的文件名，.后面并不是后缀名，这个文件没有后缀名或者说后缀名为''。
# # # 第一种方法：用sting.rfind()方法，找.
# # def get_suffix(filename, ignore_dot=True):
# #     """ 获取文件名的后缀名
# #     :param filename: 文件名
# #     :param ignore_dot: 是否忽略后缀名前面的点
# #     :return: 文件的后缀名
# #     """
# #     # 从字符串中逆向查找.第一次出现的位置,不正向的原因是可能有两个后缀点，比如readme.txt.md,后缀名是最后一个
# #     pos = filename.rfind('.')
# #     # 通过切片操作从文件名中取出后缀名
# #     if pos <= 0:
# #         return ''
# #     return filename[pos + 1:] if ignore_dot else filename[pos:]
#
# # 第二种方法：直接使用os.path模块的splitext函数，这个函数会将文件名拆分成带路径的文件名和扩展名两个部分，然后返回一个二元组，二元组中的第二个元素就是文件的后缀名（包含.），
# 如果要去掉后缀名中的.，可以做一个字符串的切片操作。
# from os.path import splitext
#
#
# def get_suffix(filename, ignore_dot=True):
#     # return splitext(filename)[1][1:]
#     str1 = splitext(filename)
#     return str1[1][1:]
#
#
# print(get_suffix('readme.txt'))
# print(get_suffix('readme.txt.md'))
# print(get_suffix('.readme'))
# print(get_suffix('readme.'))
# print(get_suffix('readme'))

# 29-关键字参数
# 不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前，否则将会引发异常。
# def is_triangle(a, b, c):  # 位置参数：positional argument，传入参数的时候对号入座即可
# def is_triangle(*, a, b, c):  命名关键字参数：keyword-only argument，写在*之后的参数，*是一个分隔符，*前面的参数都是位置参数，而*后面的参数就是命名关键字参数
# def calc(*args): 可变参数：*args，来接收任意数量的参数，但不能处理带参数名的参数。
# def calc(*args, **kwargs): 关键字参数：**kwargs，会将传入的带参数名的参数组装成一个字典，参数名就是字典中键值对的键，而参数值就是字典中键值对的值。
# Python中的函数可以使用可变参数*args和关键字参数**kwargs来接收任意数量的参数，而且传入参数时可以带上参数名也可以没有参数名，可变参数会被处理成一个元组，而关键字参数会被处理成一个字典。
# def is_triangle(a, b, c):
#     print(f'a = {a}, b = {b}, c = {c}')
#     return a + b > c and b + c > a and a + c > b
#
#
# # 调用函数传入参数不指定参数名按位置对号入座
# print(is_triangle(1, 2, 3))
# # 调用函数通过“参数名=参数值”的形式按顺序传入参数
# print(is_triangle(a=1, b=2, c=3))
# # 调用函数通过“参数名=参数值”的形式不按顺序传入参数
# print(is_triangle(c=3, a=1, b=2))

# 30-高阶函数：函数的参数和返回值可以是任意类型的对象，这就意味着函数本身也可以作为函数的参数或返回值
# 将函数作为参数和调用函数是有显著的区别的，调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可
# def calc(*args, init_value, op, **kwargs):  # init_value代表运算的初始值，op代表二元运算函数
#     result = init_value
#     for arg in args:
#         if type(arg) in (int, float):
#             result = op(result, arg)
#     for value in kwargs.values():
#         if type(value) in (int, float):
#             result = op(result, value)
#     return result
#
#
# 方法一：定义add/mul函数
# def add(x, y):
#     return x + y
#
#
# def mul(x, y):
#     return x * y
#
#
# print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))  # （0+1+2+3）+4+5=15
# print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))  # （1*1*2）*3*4*5=120
#
#
# # 方法二：python标准库中operator模块提供的add和mul函数
# import operator
#
#
# def calc(*args, init_value, op, **kwargs):  # init_value代表运算的初始值，op代表二元运算函数
#     result = init_value
#     for arg in args:
#         if type(arg) in (int, float):
#             result = op(result, arg)
#     for value in kwargs.values():
#         if type(value) in (int, float):
#             result = op(result, value)
#     return result
#
#
# print(calc(1, 2, 3, init_value=0, op=operator.add, x=4, y=5))
# print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=operator.mul))

# 31-python 内置函数
# 通常情况下，过滤（filter）、映射（map）和归约（reduce）是处理数据中非常关键的三个步骤

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# filter(function, iterable),function -- 判断函数。iterable -- 可迭代对象。
# 接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# def is_even(n):
#     return n % 2 == 0
#
#
# num = [1, 2, 3, 4, 5, 6]
# num_temp = filter(is_even, num)
# print(type(num_temp))
# num_even = list(num_temp)
# print(num_even)

# # map() 函数会根据提供的函数对指定序列做映射。
# # map(function, iterable, ...), function -- 函数,iterable -- 一个或多个序列
# # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# def square(n):
#     return n ** 2
#
#
# num = [1, 2, 3, 4, 5, 6]
# num_temp = map(square, num)
# num_new = list(num_temp)
# print(num_new)

# # reduce() 函数会对参数序列中元素进行累积。
# # 函数将一个数据集合（链表，元组等）中所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一结果
# # Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：from functools import reduce
# # reduce(function, iterable[, initializer]), function -- 函数，有两个参数, iterable -- 可迭代对象, initializer -- 可选，初始参数
# from functools import reduce
#
#
# def add(x, y):
#     return x + y
#
#
# sum1 = reduce(add, [1, 2, 3, 4, 5])
# sum2 = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# print(sum1)
# print(sum2)

# # 32-Lambda函数
# # 在使用高阶函数的时候，如果作为参数或者返回值的函数本身非常简单，一行代码就能够完成，那么可以使用Lambda函数来表示。
# Python中的Lambda函数是没有的名字函数，所以也叫做匿名函数，匿名函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值.
# # 定义Lambda函数的关键字是lambda，后面跟函数的参数，如果有多个参数用逗号进行分隔；冒号后面的部分就是函数的执行体，通常是一个表达式，表达式的运算结果就是Lambda函数的返回值，不需要写return 关键字。
# num1 = [35, 12, 8, 99, 60, 52]
# num2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, num1)))
# print(num2)


# # 33-装饰器
# # 装饰器是Python中用一个函数装饰另外一个函数或类并为其提供额外功能的语法现象。
# # 装饰器是一个高阶函数，它的参数和返回值都是函数【函数做参数和返回值只要函数名】。
# # 装饰器本身是一个函数，它的参数是被装饰的函数或类，它的返回值是一个带有装饰功能的函数。
# #     - 装饰器函数：record_time(func)
# #     - 装饰器的参数func：被装饰的函数或类，download,upload,
# #     - 装饰器的返回值return：带有装饰功能的函数，wrapper
# # 语法糖：编程语言中添加的某种语法，这种语法对语言的功能没有影响，但是使用更加方便，代码的可读性也更强，我们将其称之为“语法糖”或“糖衣语法”。
# # 可以用@装饰器函数 将装饰器函数直接放在被装饰的函数上，效果跟上面的代码相同.
#
# # # 原始代码
# # import random
# # import time
# #
# #
# # def download(filename):
# #     print(f'开始下载{filename}')
# #     time.sleep(random.randint(2, 6))
# #     print(f'{filename}下载完成。')
# #
# #
# # def upload(filename):
# #     print(f'开始上传{filename}')
# #     time.sleep(random.randint(4, 8))
# #     print(f'{filename}上传完成。')
# #
# #
# # # # 原始代码查看花费时间
# # # start = time.time()
# # # download('MySQL从删库到跑路.avi')
# # # end = time.time()
# # # print(f'花费时间：{end - start:.3f}秒')
# # #
# # # start = time.time()
# # # upload('Python从入门到住院.pdf')
# # # end = time.time()
# # # print(f'花费时间：{end - start:.3f}秒')
# #
# # # 用装饰器实现查看花费时间
# # def record_time(func):
# #     def wrapper(*args, **kwargs):
# #         start = time.time()
# #         result = func(*args, **kwargs)
# #         end = time.time()
# #         print(f'{func.__name__}执行时间：{end - start:.3f}秒！')
# #         return result
# #
# #     return wrapper
# #
# #
# # download = record_time(download)
# # upload = record_time(upload)
# # download('MySQL从删库到跑路.avi')
# # upload('Python从入门到住院.pdf')
#
# # 用语法糖之后的装饰器代码，用@装饰器函数 将装饰器函数直接放在被装饰的函数上
# import time
# import random
#
#
# def record_time(func):
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__}执行时间：{end - start:.3f}秒！')
#         return result
#     return wrapper
#
#
# @record_time    # 相当于原始代码里的download = record_time(download)
# def download(filename):
#     print(f'开始下载{filename}...')
#     time.sleep(random.randint(2, 6))
#     print(f'{filename}下载完成！')
#
#
# @record_time  # 相当于原始代码里的upload = record_time(upload)
# def upload(filename):
#     print(f'开始上传{filename}...')
#     time.sleep(random.randint(4, 8))
#     print(f'{filename}下载完成！')
#
#
# download('《MySQL从删库到跑路.avi》')
# upload('《Python从入门到住院.pdf》')


# # 34-面向对象编程
# 面向对象编程：把一组数据和处理数据的方法组成对象（object），把行为相同的对象归纳为类（class），通过封装（encapsulation）隐藏对象的内部细节，通过继承（inheritance）实现类的特化和泛化，通过多态（polymorphism）实现基于对象类型的动态分派。
# 类是一个抽象的概念，对象是一个具体的概念。
# 在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类。对象的属性是对象的静态特征，对象的行为是对象的动态特征。按照上面的说法，如果我们把拥有共同特征的对象的属性和行为都抽取出来，就可以定义出一个类。
# 使用class关键字加上类名来定义类，通过缩进我们可以确定类的代码块，就如同定义函数那样。在类的代码块中，我们需要写一些函数，我们说过类是一个抽象概念，那么这些函数就是我们对一类对象共同的动态特征的提取。写在类里面的函数我们通常称之为方法，方法就是对象的行为，也就是对象可以接收的消息。方法的第一个参数通常都是self，它代表了接收这个消息的对象本身。
# 构造器语法：类的名字后跟上圆括号就是所谓的构造器语法。
# 魔术方法/魔法方法：__（读做dunder）开头和结尾的方法通常是有特殊用途和意义的方法。
# 在很多场景下，面向对象编程其实就是一个三步走的问题。第一步定义类，第二步创建对象，第三步给对象发消息（调用对象的方法）.
#
#
# # 定义类
# class Student:  # 类
#
#     # 初始化方法：__init__方法，给学生对象定义属性，同时完成对属性赋初始值的操作
#     # 在调用Student类的构造器创建对象时，首先会在内存中获得保存学生对象所需的内存空间，然后通过自动执行__init__方法，完成对内存的初始化操作，也就是把数据放到内存空间中。
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # 方法：类里的函数，是学生对象的行为，self代表对象
#     def study(self, course_name):
#         print(f'{self.name}正在学习{course_name}.')
#
#     def play(self):   # 方法2
#         print(f'{self.name}正在玩游戏.')
#
#     # __repr__魔术方法：该方法返回的字符串就是用print函数打印对象的时候会显示的内容
#     # 使用情境：打印对象的时候不希望看到对象的地址而是看到我们自定义的信息
#     def __repr__(self):
#         return f'{self.name}:{self.age}'
#
#
# # # 创建和使用对象
# # stu1 = Student()     # 构造器语法，创建学生对象.
# # stu2 = Student()     # 定义的变量其实保存的是一个对象在内存中的逻辑地址（位置），通过这个逻辑地址，我们就可以在内存中找到这个对象
# # # print(stu1)        # 输出了对象在内存中的地址（十六进制形式）,<__main__.Student object at 0x10ad5ac50>
# # # print(stu2)
# # # print(hex(id(stu1)), hex(id(stu2))) #  id函数查看对象标识获得的值, 0x10ad5ac50 0x10ad5acd0
# #
# # 给对象发消息，即调用对象的方法
# # # 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
# # Student.study(stu1, 'Python程序设计')
# # # 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
# # stu1.study('Python程序设计')
# #
# # Student.play(stu2)
# # stu2.play()
#
# # # 由于初始化方法除了self之外还有两个参数，所以调用Student类的构造器创建对象时要传入这两个参数
# # stu1 = Student('芦蒿', 40)
# # stu2 = Student('王大锤', 15)
# # stu1.study('Python程序设计')
# # stu2.play()
#
#
# # 使用__repr__返回打印对象的时候显示的内容
# stu1 = Student('芦蒿', 40)
# print(stu1)
# students = [stu1, Student('王大锤', 25), Student('李元芳', 36)]
# print(students)


# # 35-定义一个类描述数字时钟。
# import time
#
#
# class Clock(object):
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """
#         初始化方法
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self.hour = hour
#         self.minute = minute
#         self.sec = second
#
#     def run(self):
#         """
#         走字
#         :return:
#         """
#         self.sec += 1
#         if self.sec == 60:
#             self.sec = 0
#             self.minute += 1
#             if self.minute == 60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#
#     def show(self):
#         """
#         显示时间
#         :return:
#         """
#         #  : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
#         # ^, <, > 分别是居中、左对齐、右对齐，后面带宽度。
#         # + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
#         # b、d、o、x 分别是二进制、十进制、八进制、十六进制。
#         return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.sec:0>2d}'
#
#
# clock = Clock(23, 59, 58)
# while True:
#     print(clock.show())
#     # print(time.ctime())
#     time.sleep(1)
#     # print(time.ctime())
#     clock.run()

# # 36-定义一个类描述平面上的点，要求提供计算到另一个点距离的方法。
# class Point(object):
#
#     def __init__(self, x=0, y=0):
#         """
#         初始化方法
#         :param x: 横坐标
#         :param y: 纵坐标
#         """
#         self.x, self.y = x, y
#
#     def distance_to(self, other):
#         """
#         计算与另一个点点距离
#         :param other: 另一个点
#         :return:
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return (dx * dx + dy * dy) ** 0.5
#
#     # 返回对象的字符串表达式
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# p1 = Point(3, 5)
# p2 = Point(6, 9)
# print(p1, p2)
# print(p1.distance_to(p2))

# # 37-面向对象进阶
# # class Student:
# # #  __slots__ = ('name', 'age')
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #
# # stu = Student('王大锤', 20)
# # stu.sex = '男'
#
# # 继承和多态
# # 继承：通过继承，我们可以从已有的类创建新类，实现对已有类代码的复用。
# # 继承的语法是在定义类的时候，在类名后的圆括号中指定当前类的父类
# # Python语言允许多重继承，也就是说一个类可以有一个或多个父类
# # 多态：子类继承父类的方法后，还可以对方法进行重写（重新实现该方法），不同的子类可以对父类的同一个方法给出不同的实现版本，这样的方法在程序运行时就会表现出多态行为（调用相同的方法，做了不同的事情）。
# # 多态是面向对象编程中最精髓的部分
#
# class Person:
#     """
#     人类
#     """
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f'{self.name}正在吃饭。')
#
#     def sleep(self):
#         print(f'{self.name}正在睡觉。')
#
#
# # 继承父类Person()
# class Student(Person):
#     """学生类"""
#
#     # 在子类的初始化方法中，我们可以通过super().__init__()来调用父类初始化方法
#     # super函数是Python内置函数中专门为获取当前对象的父类对象而设计的。
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def study(self, course_name):
#         print(f'{self.name}正在学习{course_name}')
#
#
# class Teacher(Person):
#     """老师类"""
#
#     # 子类除了可以通过继承得到父类提供的属性和方法外，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力.
#     # 在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，也叫做“里氏替换原则”（Liskov Substitution Principle）。
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self.title = title
#
#     def teach(self, course_name):
#         print(f'{self.name}{self.title}正在讲授{course_name}.')
#
#
# stu1 = Student('白元芳', 21)
# stu2 = Student('狄仁杰', 22)
# teacher = Teacher('武则天', 35, '副教授')
# stu1.eat()
# stu2.sleep()
# teacher.teach('Python程序设计')
# stu1.study('Python程序设计')


# # 38-扑克游戏
# # 说明：简单起见，我们的扑克只有52张牌（没有大小王），游戏需要将52张牌发到4个玩家的手上，每个玩家手上有13张牌，按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。
# from enum import Enum
#
#
# class Suit(Enum):
#     """花色（枚举）"""
#     SPADE, HEART, CLUB, DIAMOND = range(4)
#
#
# for suit in Suit:
#     print(f'{suit}: {suit.value}')


# 39-工资结算系统
# 要求：某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。其中，部门经理的月薪是固定15000元；程序员按工作时间（以小时为单位）支付月薪，每小时200元；销售员的月薪由1800元底薪加上销售额5%的提成两部分构成。


