from sklearn import preprocessing
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\DELL\Desktop\数据\空气质量_主成分分析.csv", encoding='gbk', index_col=0).reset_index(drop=True)
# print(df)
# 进行标准化
df = preprocessing.scale(df)
print(df)