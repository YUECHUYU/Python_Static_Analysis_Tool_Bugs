import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

# 读取Excel数据
df = pd.read_excel('mypy.xlsx')

# 添加工具生命周期阶段列
df['Lifecycle Stage'] = pd.cut(df['Opened'], bins=[pd.to_datetime('2012-12-08'), pd.to_datetime('2016-12-28'),
                                                   pd.to_datetime('2021-12-30'), pd.to_datetime('2023-12-19')],
                               labels=['初期（2012-12-08-2016-12-28）', '中期（2016-12-28-2021-12-30）', '后期（2021-12-30-2023-12-19）'])

# 统计每个阶段的故障症状分布
stage_counts = df.groupby(['Lifecycle Stage', 'Symptoms']).size().unstack(fill_value=0)

# 设置中文显示
font = FontProperties(fname=r"C:\Windows\Fonts\STSONG.ttf", size=12)  # 使用华文宋体

# 设置Seaborn全局字体
sns.set_theme(font='STSONG')

# 设置颜色和字体样式
sns.set_palette("pastel")  # 使用pastel调色板
dark_blue = sns.color_palette("pastel")[1]  # 获取深蓝色

# 调整深蓝色的亮度
light_dark_blue = sns.light_palette(dark_blue, as_cmap=True)

# 绘制三个饼状图
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 自定义图例标签
legend_labels = ['1.崩溃', '2.类型推断错误', '3.假阳性/阴性', '4.构建错误', '5.性能不佳', '6.语法分析错误', '7.未知']

for i, stage in enumerate(['初期（2012-12-08-2016-12-28）', '中期（2016-12-28-2021-12-30）', '后期（2021-12-30-2023-12-19）']):
    stage_data = stage_counts.loc[stage]
    stage_data = stage_data[stage_data > 0]  # 去除占比为0的部分

    # 获取调色板颜色
    colors = sns.color_palette("pastel", n_colors=len(stage_data))

    axs[i].pie(stage_data, autopct='%1.1f%%', startangle=90, colors=colors, labels=None)  # labels设置为None
    axs[i].set_title(f'{stage}', fontproperties=font)

# 添加图例
fig.legend(legend_labels, title='故障症状', loc='lower right')
plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# from matplotlib.font_manager import FontProperties
#
# # 读取Excel数据
# df = pd.read_excel('mypy.xlsx')
#
# # 添加工具生命周期阶段列
# df['Lifecycle Stage'] = pd.cut(df['Opened'], bins=[pd.to_datetime('2012-12-08'), pd.to_datetime('2016-12-28'),
#                                                    pd.to_datetime('2021-12-30'), pd.to_datetime('2023-12-19')],
#                                labels=['初期（2012-12-08-2016-12-28）', '中期（2016-12-28-2021-12-30）', '后期（2021-12-30-2023-12-19）'])
#
# # 统计每个阶段的故障症状分布
# stage_counts = df.groupby(['Lifecycle Stage', 'Symptoms']).size().unstack(fill_value=0)
#
# # 设置中文显示
# font = FontProperties(fname=r"C:\Windows\Fonts\STSONG.ttf", size=12)  # 使用华文宋体
#
# # 设置Seaborn全局字体
# sns.set_theme(font='STSONG')
#
# # 设置颜色和字体样式
# sns.set_palette("pastel")  # 使用pastel调色板
# dark_blue = sns.color_palette("pastel")[1]  # 获取深蓝色
#
# # 调整深蓝色的亮度
# light_dark_blue = sns.light_palette(dark_blue, as_cmap=True)
#
# # 绘制三个饼状图
# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
#
# # 自定义图例标签
# legend_labels = ['1.崩溃', '2.类型推断错误', '3.假阳性/阴性', '4.构建错误', '5.性能不佳', '6.语法分析错误', '7.未知']
#
# for i, stage in enumerate(['初期（2012-12-08-2016-12-28）', '中期（2016-12-28-2021-12-30）', '后期（2021-12-30-2023-12-19）']):
#     stage_data = stage_counts.loc[stage]
#     stage_data = stage_data[stage_data > 0]  # 去除占比为0的部分
#
#     # 获取调色板颜色
#     colors = sns.color_palette("pastel", n_colors=len(stage_data))
#
#     wedges, texts, autotexts = axs[i].pie(stage_data, autopct='%1.1f%%', startangle=90, colors=colors, labels=None)  # labels设置为None
#     axs[i].set_title(f'{stage}', fontproperties=font)
#
#     # 添加色块标记
#     for j, (wedge, text) in enumerate(zip(wedges, texts)):
#         angle = (wedge.theta2 + wedge.theta1) / 2.  # 计算角度的中点
#         radius = 1.07  # 设置色块标记的半径
#         x = radius * np.cos(np.deg2rad(angle))
#         y = radius * np.sin(np.deg2rad(angle))
#         axs[i].text(x, y, str(j + 1), ha='center', va='center', color='black', fontsize=12, fontweight='bold')
#
# # 添加图例
# fig.legend(legend_labels, title='故障症状', loc='lower right')
# plt.show()



