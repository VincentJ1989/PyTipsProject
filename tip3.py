# 1.eval和exec的区别(前者返回结果，后者不返回)
a = 1
exec("a=2")
print(a)
a = eval('a+2')
print(a)

# 2.生成器表达式--与for循环列表推导式不同，它不是使用方括号，而是使用圆括号
myGen = (x * x for x in range(3))
for i in myGen:
    print(i)

# 3.变量作用域
# global的使用
a = 6


def func():
    """这样才能去修改全局变量a，否则，打印的还是5"""
    global a
    a = 5


func()
print(a)
# nonglobal的使用
a = 6


def func2():
    a = 7
    
    def nested():
        """这样可以引用比其他优先基地的作用域下的变量"""
        nonlocal a
        a = 9
    
    nested()
    print(a)


func2()
print(a)


# 4.工厂函数
# 闭包函数（closure）--也叫闭合函数
def wrapperfun(strname):
    def recoder(age):
        print('姓名：', strname, '年纪：', age)
    
    # 返回recoder函数
    return recoder


fun = wrapperfun('Anna')
fun(37)
fun = wrapperfun('Gary')
fun(45)

# 5.装饰器
# fn是需要被装饰的函数，相当于闭合函数
import functools


def checkParams(fn):
    # 方法②使用内置的functools,下面一句话的意思是将wrapper的函数名称变成与传入的fn函数一样的函数名称
    @functools.wraps(fn)
    def wrapper(strname):
        # 判断是否是字符串
        if isinstance(strname, (str)):
            return (fn(strname))
        print('variable strname is not a string type')
        return
    
    # 方法①这句话的意思是将函数名称属性恢复，避免出现装饰完后函数名字变化的现象
    # wrapper().__name__ = fn.__name__
    return wrapper


# @checkParams
def wrapperfun(strname):
    def recoder(age):
        print('姓名：', strname, '年纪：', age)
    
    return recoder


# 这一步当然也可以通过在wrapperfun函数上使用@checkParams来省略
wrapperfun2 = checkParams(wrapperfun)
fun = wrapperfun2('anna')
fun(88)
fun = wrapperfun2(37)


# 6.更高级的装饰器
# 6.1 能接收任何参数的通用参数装饰器--使用字典和元组的解包作为形参
def checkParam(fn):
    def wrapper(*arg, **kwargs):
        if isinstance(arg[0], (str)):
            return fn(*arg, **kwargs)
        print('variable strname is not a string type')
        return
    
    return wrapper


# 6.2 可接收参数的通用装饰器--在外部再套一层，可以指定模块使用
def isadmin(userid):
    def checkParam(fn):
        def wrapper(*arg, **kwargs):
            
            if userid != 'admin':
                print('Operation is prohibited sa you are not admin !')
                return
            if isinstance(arg[0], (str)):
                return fn(*arg, **kwargs)
            print('variable strname is not a string type')
            return
        
        return wrapper
    
    return checkParam


@isadmin(userid='admin')
def wrapperfun(strname):
    def recoder(age):
        print('姓名：', strname, '年纪：', age)
    
    return recoder


@isadmin(userid='anna')
def wrapperfun2(strname):
    def recoder(age):
        print('姓名：', strname, '年纪：', age)
    
    return recoder


fun = wrapperfun('anna')
fun(66)
fun = wrapperfun2(36)


# 6.3 组合装饰--多个装饰联合使用--堆叠起来即可。载入顺序是紫霞而上的，而调用顺序是自上而下的。
# 在整个代码载入的时候，装饰器就开始执行，自下而上的载入装饰器函数。（类似于压栈弹栈）

# 7. 解决"通作用域下默认参数被覆盖"问题--场景:循环生成工厂函数，其循环体作用域下的默认参数只会被覆盖
# 错误代码--打印出来的2个值是一样的都是：姓名： Anna 年纪： 43
def recoder(strname, age):
    print('姓名：', strname, '年纪：', age)


def makerecoders():
    acts = []
    for i in ['Gary', 'Anna']:
        acts.append(lambda age: recoder(i, age))
    return acts


for a in (makerecoders()):
    a(age=43)


# 因为咋循环时后面的变量覆盖了前面的变量
# 解决方案：不能将默认值放到作用域控件来存储，必须要将默认值当做参数传入到原函数recoder中
# 正确代码如下：
def recoder(strname, age):
    print('姓名：', strname, '年纪：', age)


def makerecoders():
    acts = []
    for i in ['Gary', 'Anna']:
        acts.append(lambda age, i=i: recoder(i, age))
    return acts


for a in (makerecoders()):
    a(age=54)
