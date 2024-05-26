import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 设置字体为Times New Roman
plt.rc('font',family='Times New Roman')

# 创建包含mypy和pyright讨论主题数量的DataFrame
data = {
    'mypy': [13, 27, 4, 9, 11, 2, 1],
    'pyright': [14, 18, 8, 4, 6, 2, 5]
}
df = pd.DataFrame(data)

# 计算斯皮尔曼相关系数
corr = df.corr(method='spearman')

# 创建用于掩盖相关系数的布尔矩阵
x = np.array([[False, True],
              [False, False]])

# 创建图形
f, ax = plt.subplots(figsize=(10, 8))

# 设置刻度字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# 绘制热力图
sns.heatmap(corr, center=0, annot=True, cmap='YlGnBu', mask=x, annot_kws={"size": 18}, cbar=False)

# 保存图像
plt.savefig('mypy_pyright_correlation.png')

# 显示图形
plt.show()


