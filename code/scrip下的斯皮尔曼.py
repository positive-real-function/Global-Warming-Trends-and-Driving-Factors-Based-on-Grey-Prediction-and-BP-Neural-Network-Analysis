import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

location = r"C:\Users\DELL\Desktop\数据\空气质量_主成分分析"
data = pd.read_csv(location+".csv",encoding="utf-8")
# print(data)
# result=data.corr(method="pearson")
# print(result)


myfont = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf', size=40)
sns.set(font=myfont.get_name(), color_codes=True)
# corr = df.corr(method='pearson')  # 使用皮尔逊系数计算列与列的相关性
# corr = df.corr(method='kendall')  # 肯德尔秩相关系数
data_corr = data.corr(method='spearman')  # 斯皮尔曼秩相关系数
# data_corr = data.corr(method='pearson')  # 使用皮尔逊系数计算列与列的相关性
plt.figure(figsize=(20, 15))  # figsize可以规定热力图大小
fig = sns.heatmap(data_corr, annot=True, fmt='.2g', annot_kws={'fontsize': 20})  # annot为热力图上显示数据；fmt='.2g'为数据保留两位有效数字
print(fig)
fig.get_figure().savefig(location + '_S.png')  # 保留图片
