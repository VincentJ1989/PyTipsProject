# 主要是记录一些文件操作--数据持久化的一种方法

# 1.读写文件
f = open("a.txt", 'w')
f.write("哈哈哈")
f.close()
f = open('a.txt', 'r')
s = f.read()
print(s)

import os

# 如果是以二进制打开，则只能以二进制写入
f = open('a.txt', 'wb+')
f.write(b'I like Python')
f.close()
# 删除之前需要进行close
os.remove('a.txt')

# 把文件对象当作迭代器来读取
f = open('a.txt', 'wb+')
f.write(b'I like python!\n')
f.write(b'I love python')
f.close()
f = open('a.txt', 'r+')
for line in f:
    print(line)

f.close()
os.remove('a.txt')

