# 1. 一个是养成写函数注释的习惯，另一个可以看到返回值可以是多个值
def getrecoder():
    """该函数式返回用户名字和年龄"""
    name = 'Gary'
    age = 32
    return name, age


# 函数的文档字符串存储在__doc__中
print(getrecoder.__doc__)

# 2.使用return语句可以一次返回多个值，可以定义多个变量来接收，也可以使用一个元组来接收
myName, myAge = getrecoder()
person = getrecoder()
print(person)
# 有时候只需要返回值中的某一个，可以使用(_)来过滤不接收的值
personname, _ = getrecoder()
print(personname)


# 3.带星号定义参数的注意点
def recoder(strname, *, age):
    print('姓名：', strname, "年纪：", age)


recoder('Garg', age=32)


# 下面是错误，必须指定参数名称
# recoder("Gary", 32)

# 4.混合使用形参的注意点
# 4.1 字典和元组的解包参数
def record2(*person1, **person2):
    if len(person1) != 0:
        print("元组的形参接收到内容")
    if len(person2) != 0:
        print("字典的形参接收到内容")


# p1接收
record2('Garg', 32)
# p2接收
record2(age=32, name='Gary')
# p1和p2同时接收--不指定形参的实参在前，指定形参的实参在后
record2('Gary', 32, age=32, name="Gary")
# 下面是错误的传参
# record2(age=32, name='Gary', 'Gary', 32)

# 5.匿名函数的使用---可以类比Java8，函数式一等公民
r = lambda x, y: x * y
print(r(2, 3))

# 6.reduce函数的使用--一般用于归并性任务
from functools import reduce

# 实现的功能就是1+2+3+...+101
print(reduce(lambda x, y: x + y, range(1, 101)))
# 7.map函数的使用--参考RxJava的map--一般用于映射任务
t = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(t))
# 取短的为准
t = map(lambda x, y: x + y, [1, 2, 3, 4, 5], [5, 4, 3, 2])
print(list(t))

# 8. filter函数使用--过滤性任务
t = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(tuple(t))
# 顺便看下__next__()函数的使用
t = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(t.__next__())
print(t.__next__())

# 8.看看偏函数为何物--partial关键字
from functools import partial


def person_def(name, age):
    print(name + '>>>' + str(age))


Wrapperson = partial(person_def, name="Gary")
Wrapperson(age=23)
