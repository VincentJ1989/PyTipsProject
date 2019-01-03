# 带有异常处理的文件操作
import os

try:
    f = open('a.txt', 'wb+')
    f.write('I like python')
except Exception as e:
    print(e)
    f.write(b'I love python')
finally:
    print('关闭文件')
    f.close()

try:
    f = open('a.txt', 'r+')
    for line in f:
        print(line)
finally:
    f.close()
    os.remove('a.txt')

# 使用with语句简化上面的代码--使用with可以不需要关注事后的事情。当with作用域内的语句执行完毕后，就会自动调用f.close函数
with open('a.txt', 'wb+') as f:
    try:
        print('以下是with语句的简化操作')
        f.write('I like python')
    except Exception as e:
        print(e)
        f.write(b'I love python')

with open('a.txt', 'r+') as f:
    for line in f:
        print(line)

os.remove('a.txt')
