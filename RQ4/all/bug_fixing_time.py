import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import matplotlib.font_manager as fm
plt.rc('font',family='Times New Roman')
# 设置字体为宋体
font_path = r"C:\Windows\Fonts\STSONG.ttf"
prop = fm.FontProperties(fname=font_path)

print('---------------------------------mypy---------------------------------------')
df_mypy=pd.read_excel('mypy.xlsx', engine='openpyxl')
df_mypy['Opened']=pd.to_datetime(df_mypy['Opened'])
df_mypy['Closed']=pd.to_datetime(df_mypy['Closed'])
leadtime3=(df_mypy['Closed'] - df_mypy['Opened']).map(lambda x:x.days)
df_mypy['Duration_Date']=leadtime3

mypy_day_um_list=df_mypy['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_mypy['Duration_Date'].mean())
print('median: ', df_mypy['Duration_Date'].median())
print('std: ',df_mypy['Duration_Date'].std())
print('max: ',df_mypy['Duration_Date'].max())
print('min: ',df_mypy['Duration_Date'].min())

print('---------------------------------pyright---------------------------------------')
df_pyright=pd.read_excel('pyright.xlsx', engine='openpyxl')

df_pyright['Opened']=pd.to_datetime(df_pyright['Opened'])
df_pyright['Closed']=pd.to_datetime(df_pyright['Closed'])
leadtime3=(df_pyright['Closed'] - df_pyright['Opened']).map(lambda x:x.days)
df_pyright['Duration_Date']=leadtime3
pyright_day_um_list=df_pyright['Duration_Date'].values.tolist()


print('Duration_Date:  ')
print('mean: ', df_pyright['Duration_Date'].mean())
print('median: ', df_pyright['Duration_Date'].median())
print('std: ',df_pyright['Duration_Date'].std())
print('max: ',df_pyright['Duration_Date'].max())
print('min: ',df_pyright['Duration_Date'].min())


print('------------------------draw picture!------------------------')
#,defaultreallimits=(1,1000) 从小于1开始算个数
res_mypy=stats.cumfreq(mypy_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
res_pyright=stats.cumfreq(pyright_day_um_list, numbins=1000, defaultreallimits=(0, 1000))

lowerlimit_mypy=res_mypy.lowerlimit
lowerlimit_pyright=res_pyright.lowerlimit
lowerlimit=(lowerlimit_mypy+lowerlimit_pyright)/2

#柱形的宽度
binsize_mypy=res_mypy.binsize
binsize_pyright=res_pyright.binsize
binsize=(binsize_mypy+binsize_pyright)/2

#柱形的高度(x中的数值有多少个会积累落入该柱形中,元素的个数)
cumcount_mypy=res_mypy.cumcount #其实就是res_mypy[0]
cumcount_pyright=res_pyright.cumcount
cumcount=(cumcount_mypy+cumcount_pyright)/2
x1= lowerlimit_mypy + np.linspace(0, binsize_mypy * cumcount_mypy.size, cumcount_mypy.size)
x2=lowerlimit_pyright+np.linspace(0,binsize_pyright*cumcount_pyright.size,cumcount_pyright.size)
x=lowerlimit+np.linspace(0,binsize*cumcount.size,cumcount.size)


fig=plt.figure(figsize=(12, 8), dpi=100)

ax = fig.add_subplot(1,1,1)  #（xxx）这里前两个表示几*几的网格，最后一个表示第几子图
#plt.rcParams['font.sans-serif']='Arial'
ax.set_ylim(0, 1.01)
ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])

plt.xticks([0,7,50,100,200,300,400,500,600,721,800,900,1000],fontsize=14)
plt.yticks(fontsize=14)
plt.plot(x1,res_mypy[0] / 1129, label="mypy",color='b') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x2,res_pyright[0] / 1909, label="pyright",color ='r') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")


print(res_mypy[0][721]/1129)
print(res_pyright[0][7]/1909)
plt.xlabel("bug修复时间",fontsize=16,labelpad = 6,fontproperties=prop)
plt.ylabel("bug比例",fontsize=16,labelpad = 6,fontproperties=prop)

plt.legend(loc='lower right',fontsize=16)
#plt.xticks([1,100,200,300,400,500,800])
#plt.yticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
# 添加网格线
plt.grid(linestyle="--", alpha=0.5)
plt.savefig('Bug-Fixing_Time.png')
print(plt.show())