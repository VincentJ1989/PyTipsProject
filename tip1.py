# 1.把2数中的最大值赋值给另一个变量
# 正常写法
a = 4
b = 5
if a > b:
    c = a
else:
    c = b
print(c)
# 简化写法
# 第二个方括号为假，则取第一个方括号的第一个元素；反之则取第二个元素
c = [a, b][a < b]
print(c)

# 2.使用副本来规避在应用for循环遍历修改数据时出现的死循环
words = ['I', "love", "python"]

# for items in words:// 这是错误的写法
for items in words[:]:
    words.insert(0, items)
    print(items)
print(words)

# 3.冒泡排序
n = [5, 8, 10, 1]
print('源数据：', n)


def bubble_sort(n):
    for i in range(len(n) - 1):
        for j in range(len(n) - 1 - i):
            if n[j] > n[j + 1]:
                """交换2数"""
                n[j], n[j + 1] = n[j + 1], n[j]
    
    return n


print('排序后：', bubble_sort(n))

# 4.zip的使用
# 当zip对象(t)被转化后，就会自动销毁，所以再使用t，将得不到具体的元素。
x = [1, 2, 3]
y = [3, 2, 'hello']
t = zip(x, y)
# 转成元组
# print(tuple(t))
# 转成列表
# print(list(t))
# 加*表示unzip，和zip一样，使用后自动销毁
print(*t)
# 当2个序列长度不一样时，以短的为主
# zip和for的结合使用
x = [1, 2, 3, 4, 5, 6]
y = [3, 2, 'hello']
for t1, t2 in zip(x, y):
    print(t1, t2)

# 5.使用enumerate遍历序列容器，生成带序号的新序列数据,，每个元素都是个元素
x = ['hello', 5, 6]
t = enumerate(x)
print(tuple(t))

for i, t2 in enumerate(x):
    print(i, t2)

# 6.使用列表推导式打印9*9乘法表

for x in range(1, 10):
    list = ['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]
    for i in range(len(list)):
        print(list[i], end=' ')
    print('')
