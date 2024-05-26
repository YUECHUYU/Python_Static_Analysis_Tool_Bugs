# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
#
# # 设置中文显示
# font = FontProperties(fname=r"C:\Windows\Fonts\STSONG.ttf", size=12)  # 使用华文宋体
#
# # 设置Seaborn全局字体
# sns.set_theme(font='STSONG')
#
# # 预先设定两个工具的数据
# categories = ['bug根源争议', 'bug修复方法', '性能优化', '版本发布和更新', '工具扩展性', '新功能开发', '用户体验']
# mypy_data = [13, 27, 4, 9, 11, 2, 1]
# pyright_data = [14, 18, 8, 4, 6, 2, 5]
#
# df = pd.DataFrame({
#     '讨论主题': categories,
#     'mypy': mypy_data,
#     'pyright': pyright_data
# })
#
# # 设置颜色和字体样式
# sns.set_palette("viridis", n_colors=len(categories))
#
# # 绘制堆积柱形图
# plt.figure(figsize=(10, 6))
# ax = sns.barplot(x='讨论主题', y='mypy', data=df, label='mypy', color='lightblue')
# ax = sns.barplot(x='讨论主题', y='pyright', data=df, bottom=df['mypy'], label='pyright', color='pink')
#
# # 在每个bar上添加中文标签
# for i, (mypy_val, pyright_val) in enumerate(zip(df['mypy'], df['pyright'])):
#     ax.text(i, mypy_val / 2, str(mypy_val), color='black', va='center', ha='center', fontproperties=font)
#     ax.text(i, mypy_val + pyright_val / 2, str(pyright_val), color='black', va='center', ha='center', fontproperties=font)
#
# # 设置图表标题和坐标轴标签
# plt.xlabel('讨论主题', fontproperties=font)
# plt.ylabel('数量', fontproperties=font)
#
# # 设置y轴刻度的中文标签
# plt.yticks(fontproperties=font)
#
# # 显示图表
# plt.legend()
# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文显示
font = FontProperties(fname=r"C:\Windows\Fonts\STSONG.ttf", size=15)  # 使用华文宋体

# 设置Seaborn全局字体
sns.set_theme(font='STSONG')

# 预先设定两个工具的数据
categories = ['bug根源争议', 'bug修复方法', '性能优化', '版本发布和更新', '工具扩展性', '新功能开发', '用户体验']
mypy_data = [13, 27, 4, 9, 11, 2, 1]
pyright_data = [14, 18, 8, 4, 6, 2, 5]

df = pd.DataFrame({
    '讨论主题': categories,
    'mypy': mypy_data,
    'pyright': pyright_data
})

# 设置颜色和字体样式
sns.set_palette("viridis", n_colors=len(categories))

# 绘制堆叠柱形图
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='讨论主题', y='mypy', data=df, label='mypy', color='lightblue')
ax = sns.barplot(x='讨论主题', y='pyright', data=df, bottom=df['mypy'], label='pyright', color='pink', hatch='//')  # 添加底纹

# 在每个bar上添加中文标签
for i, (mypy_val, pyright_val) in enumerate(zip(df['mypy'], df['pyright'])):
    ax.text(i, mypy_val / 2, str(mypy_val), color='black', va='center', ha='center', fontproperties=font)
    ax.text(i, mypy_val + pyright_val / 2, str(pyright_val), color='black', va='center', ha='center', fontproperties=font)

# 设置图表标题和坐标轴标签
plt.xlabel('讨论主题', fontproperties=font)
plt.ylabel('数量', fontproperties=font)

# 设置y轴刻度的中文标签
plt.yticks(fontproperties=font)

# 显示图例和图表
plt.legend()
plt.show()
