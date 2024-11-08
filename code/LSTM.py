import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense,Dropout
from numpy import concatenate
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from math import sqrt

#设置随机数种子
import tensorflow as tf
tf.random.set_seed(2)

#导入数据集
qy_data=read_csv(r'C:\Users\HUAWEI\Desktop\abc.csv',parse_dates=['num'],index_col='num')
qy_data.index.name='num' #选定索引列

#打印前五列进行查看
print(qy_data.head())

#数据处理
# 获取DataFrame中的数据，形式为数组array形式
values = qy_data.values
# 确保所有数据为float类型
values = values.astype('float32')

#归一化处理
#使用MinMaxScaler缩放器，将全部数据都缩放到[0,1]之间，加快收敛。
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)

#将时间序列转换为监督学习问题
#将时间序列形式的数据转换为监督学习集的形式，例如：[[10],[11],[12],[13],[14]]转换为[[0,10],[10,11],[11,12],[12,13],[13,14]]，即把前一个数作为输入，后一个数作为对应输出。
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
        # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg


reframed = series_to_supervised(scaled, 2, 1)

