# 字符串与二进制的相互转化
# 需要注意的是二进制与文本的相互转化依赖于编码格式、操作系统等因素。
# 将字符串转化为二进制数
# 方式1
b1 = b'I like python'
# 方式2
b2 = bytes('I love python', 'utf-8')

print(b1, b2, sep=';')

# 二进制转字符串--需要注意的一点是windows和linux下编码格式的不同
b = bytes('I like python', 'utf-8')
print(b, b.decode('utf-8'), sep=';')

import os
# 使用pickle函数进行序列化--缺点：不支持并发访问，故而需要ZODB模块来支持
import pickle

tup1 = ('I like python', [1, 2, 3], None)

# dumps与loads
p1 = pickle.dumps(tup1)
t2 = pickle.loads(p1)

print(t2)

# dump与load
path = 'a.pkl'
with open(path, 'wb') as f:
    # 第三个是转码协议
    # dump的file必须有write方法
    pickle.dump(tup1, f, pickle.HIGHEST_PROTOCOL)

with open(path, 'rb') as f:
    # load的file必须要有read和readline
    t3 = pickle.load(f)
    print(t3)

os.remove(path)

