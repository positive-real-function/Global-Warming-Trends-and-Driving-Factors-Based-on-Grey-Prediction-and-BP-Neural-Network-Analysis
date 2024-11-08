import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import mpl
from matplotlib.pyplot import MultipleLocator

# import data
file_path = '各地区每月平均温度.csv'
raw_data = pd.read_csv(file_path, encoding='GBK')
raw_data_li = raw_data.values.tolist()
data1 = []
data2 = []
data3 = []
data_ym = []
# 热带
for s_li in raw_data_li:
    data1.append(s_li[4])
# 南温带
for s_li in raw_data_li:
    data2.append(s_li[5])
# 北温带
for s_li in raw_data_li:
    data3.append(s_li[6])
# 年月
for s_li in raw_data_li:
    data_ym.append(s_li[0])


def mktest(inputdata):
    import numpy as np
    inputdata = np.array(inputdata)
    n = inputdata.shape[0]
    Sk = np.zeros(n)
    UFk = np.zeros(n)
    r = 0
    for i in range(1, n):
        for j in range(i):
            if inputdata[i] > inputdata[j]:
                r = r + 1
        Sk[i] = r
        E = (i + 1) * i / 4
        Var = (i + 1) * i * (2 * (i + 1) + 5) / 72
        UFk[i] = (Sk[i] - E) / np.sqrt(Var)

    Sk2 = np.zeros(n)
    UBk = np.zeros(n)
    inputdataT = inputdata[::-1]
    r = 0
    for i in range(1, n):
        for j in range(i):
            if inputdataT[i] > inputdataT[j]:
                r = r + 1
        Sk2[i] = r
        E = (i + 1) * (i / 4)
        Var = (i + 1) * i * (2 * (i + 1) + 5) / 72
        UBk[i] = -(Sk2[i] - E) / np.sqrt(Var)
    UBk2 = UBk[::-1]
    return UFk, UBk2


mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止标题出现乱码。
plt.rcParams['axes.unicode_minus'] = False  # 防止出现图上的负数为方框。

# y值和x值   分别输入六个站点的最大冻土深度值，将值以列表的方式导入
# a = data1
# a = data2
a = data3
x_values = data_ym
uf, ub = mktest(a)

plt.figure(figsize=(8, 4))  # 图片的大小
plt.plot(uf, 'r', label='UFk')
plt.plot(ub, 'b', label='UBk')
# plt.xticks([0,12, 24, 36, 48, 60 ,72, 84, 96, 108, 120, ],
#            ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', ])
# 将默认的x轴数值替换为年份的X轴，默认是0-61，一共62个值，代表X轴内容。
plt.xticks([0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200, 1320, 1440,],
           ['1900', '1910', '1920', '1930', '1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010' , '2020'])

# 0.01显著性检验
x_lim = plt.xlim()
plt.plot(x_lim,[-1.96,-1.96],linestyle = (0,(6,6)),color = 'r')
plt.plot(x_lim, [0,0],linestyle = (0,(6,6)))
plt.plot(x_lim,[1.96,1.96],linestyle = (0,(6,6)),color = 'r')
plt.legend()
# 设置图片的标签（标题）
plt.title("北温带平均气温突变检验表")  # x轴上的名字
plt.xlabel("年份（1899年-2022年）")  # x轴上的名字
plt.ylabel("突变值波动参数")  # y轴上的名字
plt.grid()  # 形成网格线输出
x_major_locator = MultipleLocator(5)
plt.show()

