# ZODB应用的例子--处理并发访问序列化
import os

import pydicom
import pylab


def load_scan(path):
    """加载数据"""
    slices = [pydicom.read_file(path + '/' + s) for s in os.listdir(path)]
    return slices


# 指定文件路径
INPUT_FOLDER = 'patient32/P32dicom'
first_patient = load_scan(INPUT_FOLDER)
# 将第一个数据打印出来
print(first_patient[0])

print(first_patient[0].dir())
# 输出所有属性名中含有pat的字符串属性
print(first_patient[0].dir('pat'))
print(first_patient[0].PatientName)

# 显示单张数据图像
print('显示单张数据图像')
pylab(first_patient[0].pixel_array, cmap=pylab.cm.bone)
pylab.show()

# 批量生产数据图像
print('批量生产数据图像')
import PIL.Image as Image
import math


def plot_ct_scan(scan):
    length = len(scan)
    each_size = int(math.sqrt(float(810 * 810) / length))
    lines = int(810 / each_size)
    # 生成白背景
    image = Image.new('RGB', (810, 810), 'white')
    x = 0
    y = 0
    for i in range(0, length):
        # 生成img对象
        img = Image.fromarray(scan[i].pixel_array.astype(int))
        # 调整图片大小
        img = img.resize(each_size, each_size, Image.ANYIALIAS)
        # 拼接图片
        image.paset(img, x * each_size, y * each_size)
        x += 1
        if x == lines:
            x = 0
            y += 1
        # 保存图片
        image.save('./' + 'all.jpg')


plot_ct_scan(first_patient)
