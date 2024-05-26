import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文显示
font = FontProperties(fname=r"C:\Windows\Fonts\STSONG.ttf", size=15)  # 使用华文宋体

# 设置Seaborn全局字体
sns.set_theme(font='STSONG')

# 预先设定症状的名称和数量
data = {'symptom': ['假阳性/阴性', '类型推断错误', '语法分析错误', '崩溃', '构建错误', '未知', '性能不佳'],
        'num': [365, 277, 173, 112, 89, 61, 52]}

df = pd.DataFrame(data)

# 设置颜色和字体样式
palette = sns.color_palette("viridis", n_colors=len(df))
sns.set(font_scale=1.0)

# 绘制故障分布情况图
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='symptom', y='num', data=df, palette=palette)

# 在每个bar上添加中文标签和数量数字
for i, v in enumerate(df['num']):
    ax.text(i, v + 1, str(v), color='black', ha='center', fontproperties=font)

# 设置图表标题和坐标轴标签（使用SimSun字体）
# plt.title('症状划分的故障分布情况图', fontproperties=font)
plt.ylabel('故障数量', fontproperties=font)
plt.xlabel('症状', fontproperties=font)

# 设置x轴刻度的中文标签
plt.xticks(range(len(df['symptom'])), df['symptom'], fontproperties=font)

# 设置y轴刻度为每50一格
plt.yticks(range(0, max(df['num'])+1, 50), fontproperties=font)

# 显示图表
plt.show()
