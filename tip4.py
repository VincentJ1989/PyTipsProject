# 1.异常的处理
import sys
import traceback


def catchExp():
    try:
        x = int(input('请输入一个数字'))
        print('30除以', x, "等于", 30 / x)
    # 也可以分开写
    # 增加as e：可以获取异常类型
    except (ZeroDivisionError, ValueError) as e:
        print(e)
        # 需要输出详细的报错信息方案①
        print(sys.exc_info())
        # 需要输出详细的报错信息方案②
        traceback.print_tb(sys.exc_info()[2])
        # traceback.print_exc()
        print('输入异常,重新输入...')
    except:
        print('其他异常...')
    # 没有异常发生时，走else
    else:
        print('无异常发生，再见')


# 2.创建异常，即抛出异常
def throwExp():
    try:
        x = int(input('请输入一个除数数字'))
        if 0 == x:
            raise ValueError('输入错误，0不能作为除数')
        print(30 / x)
    except Exception as e:
        print(e)
    else:
        print('计算结果：30/', x, 30 / x)


# 3.finally使用
def withFinally():
    try:
        print('打开一个文件')
        print('读取内容')
        raise IOError("读取出错")
    except Exception as e:
        print(e)
    finally:
        print('关闭文件')
        
# 4.断言的使用
assert 1!=1,('1不等于1，报错')
