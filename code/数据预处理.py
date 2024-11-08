import numpy as np
import pandas as pd

# data_APMCM_C.dropna()


data_APMCM_C = pd.read_csv("2022_APMCM_C_Data.csv", encoding="gbk")
# print(data_APMCM_C.describe())
# print(data_APMCM_C.isnull().sum(axis=0))
# print(data_APMCM_C['dt'])
data_APMCM_C.loc[:, 'dt'] = pd.to_datetime(data_APMCM_C.loc[:, 'dt'], format='%Y-%m-%d', errors='coerce')
data_APMCM_C.set_index('dt', inplace=True)

result=data_APMCM_C['1899':'2012']
# print(result)
print(result.isnull().sum(axis=0))
result.to_csv('1899-2012.csv')
# data_delete = data_APMCM_C.dropna()
# data_delete.to_csv('data_delete.csv')

# 将缺失值填充为nan
# result_nan = data_delete.fillna(0, inplace=False)
# 将0赋值为NAN
# result_nan['AverageTemperature']=result_nan['AverageTemperature'].replace({0:np.NAN})
# result_nan['AverageTemperatureUncertainty']=result_nan['AverageTemperatureUncertainty'].replace({0:np.NAN})
# print(result_nan)


# print(result_nan.loc['1834-01-01','AverageTemperature'])

# for i in result_nan:
#     if result_nan['City']=='Kabul':
#         print(result_nan['AverageTemperatureUncertainty'])
# j = 0
# for i in result_nan['month']:
#     if i == 1:
#         sum += result_nan['AverageTemperatureUncertainty'].values
#         j += 1
# aver = sum / j
# print(aver)
