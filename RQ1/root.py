import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文显示
font = FontProperties(fname=r"C:\Windows\Fonts\STSONG.ttf", size=15)  # 使用华文宋体

# 设置Seaborn全局字体
sns.set_theme(font='STSONG')

# 预先设定10个根本原因的名称和数量
data = {'root': ['错误的算法实施', '异常处理不当', '错误的配置', '错误的条件逻辑', '错误的赋值', '其他', '缺失条件检查', '环境不兼容', '内存', '并发'],
        'num': [440, 209, 156, 108, 58, 52, 51, 23, 22, 10]}

df = pd.DataFrame(data)

# 设置颜色和字体样式
palette = sns.color_palette("viridis", n_colors=len(df))
sns.set(font_scale=1.0)

# 绘制故障分布情况图
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='num', y='root', data=df, palette=palette)

# 在每个bar上添加中文标签
for i, v in enumerate(df['num']):
    ax.text(v + 1, i, str(v), color='black', va='center', fontproperties=font)

# 设置图表标题和坐标轴标签（使用SimSun字体）
# plt.title('根本原因划分的故障分布情况图', fontproperties=font)
plt.xlabel('故障数量', fontproperties=font)
plt.ylabel('根本原因', fontproperties=font)

# 设置y轴刻度的中文标签
plt.yticks(range(len(df['root'])), df['root'], fontproperties=font)

# 设置x轴刻度为每50一格
plt.xticks(range(0, max(df['num'])+1, 50), fontproperties=font)

# 显示图表
plt.show()
