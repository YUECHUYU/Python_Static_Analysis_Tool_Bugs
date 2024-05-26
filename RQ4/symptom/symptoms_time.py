# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import scipy.stats as stats
# import matplotlib.font_manager as fm
# plt.rc('font',family='Times New Roman')
# # 设置字体为宋体
# font_path = r"C:\Windows\Fonts\STSONG.ttf"
# prop = fm.FontProperties(fname=font_path)
#
# print('---------------------------------positive---------------------------------------')
# df_positive=pd.read_excel('3.false positive.xlsx', engine='openpyxl')
# df_positive['Opened']=pd.to_datetime(df_positive['Opened'])
# df_positive['Closed']=pd.to_datetime(df_positive['Closed'])
# leadtime3=(df_positive['Closed'] - df_positive['Opened']).map(lambda x:x.days)
# df_positive['Duration_Date']=leadtime3
#
# positive_day_um_list=df_positive['Duration_Date'].values.tolist()
#
# print('Duration_Date:  ')
# print('mean: ', df_positive['Duration_Date'].mean())
# print('median: ', df_positive['Duration_Date'].median())
# print('std: ',df_positive['Duration_Date'].std())
# print('max: ',df_positive['Duration_Date'].max())
# print('min: ',df_positive['Duration_Date'].min())
#
# print('---------------------------------type---------------------------------------')
# df_type=pd.read_excel('2.incorrect type.xlsx', engine='openpyxl')
#
# df_type['Opened']=pd.to_datetime(df_type['Opened'])
# df_type['Closed']=pd.to_datetime(df_type['Closed'])
# leadtime3=(df_type['Closed'] - df_type['Opened']).map(lambda x:x.days)
# df_type['Duration_Date']=leadtime3
# type_day_um_list=df_type['Duration_Date'].values.tolist()
#
# print('Duration_Date:  ')
# print('mean: ', df_type['Duration_Date'].mean())
# print('median: ', df_type['Duration_Date'].median())
# print('std: ',df_type['Duration_Date'].std())
# print('max: ',df_type['Duration_Date'].max())
# print('min: ',df_type['Duration_Date'].min())
#
# print('---------------------------------syntax---------------------------------------')
# df_syntax=pd.read_excel('6.incorrect syntax.xlsx', engine='openpyxl')
# df_syntax['Opened']=pd.to_datetime(df_syntax['Opened'])
# df_syntax['Closed']=pd.to_datetime(df_syntax['Closed'])
# leadtime3=(df_syntax['Closed'] - df_syntax['Opened']).map(lambda x:x.days)
# df_syntax['Duration_Date']=leadtime3
#
# syntax_day_um_list=df_syntax['Duration_Date'].values.tolist()
#
# print('Duration_Date:  ')
# print('mean: ', df_syntax['Duration_Date'].mean())
# print('median: ', df_syntax['Duration_Date'].median())
# print('std: ',df_syntax['Duration_Date'].std())
# print('max: ',df_syntax['Duration_Date'].max())
# print('min: ',df_syntax['Duration_Date'].min())
#
# print('------------------------draw picture!------------------------')
# #,defaultreallimits=(1,1000) 从小于1开始算个数
# res_positive=stats.cumfreq(positive_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
# res_type=stats.cumfreq(type_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
# res_syntax=stats.cumfreq(syntax_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
#
# lowerlimit_positive=res_positive.lowerlimit
# lowerlimit_type=res_type.lowerlimit
# lowerlimit_syntax=res_syntax.lowerlimit
# lowerlimit=(lowerlimit_type+lowerlimit_positive+lowerlimit_syntax)/3
#
# #柱形的宽度
# binsize_positive=res_positive.binsize
# binsize_type=res_type.binsize
# binsize_syntax=res_syntax.binsize
# binsize=(binsize_type+binsize_positive+binsize_syntax)/3
#
# #柱形的高度(x中的数值有多少个会积累落入该柱形中,元素的个数)
# cumcount_positive=res_positive.cumcount
# cumcount_type=res_type.cumcount
# cumcount_syntax=res_syntax.cumcount
# cumcount=(cumcount_type+cumcount_positive+cumcount_syntax)/3
#
# x1= lowerlimit_positive + np.linspace(0, binsize_positive * cumcount_positive.size, cumcount_positive.size)
# x2=lowerlimit_type+np.linspace(0,binsize_type*cumcount_type.size,cumcount_type.size)
# x3= lowerlimit_syntax + np.linspace(0, binsize_syntax * cumcount_syntax.size, cumcount_syntax.size)
# x=lowerlimit+np.linspace(0,binsize*cumcount.size,cumcount.size)
#
#
# fig=plt.figure(figsize=(12, 8), dpi=100)
#
# ax = fig.add_subplot(1,1,1)  #（xxx）这里前两个表示几*几的网格，最后一个表示第几子图
# #plt.rcParams['font.sans-serif']='Arial'
# ax.set_ylim(0, 1.01)
# ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
#
# plt.xticks([0,100,200,300,351,400,509,600,700,800,900,1000],fontsize=14)
# plt.yticks(fontsize=14)
# plt.plot(x1,res_positive[0] / 365, label="假阳性/阴性",color='b') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
# plt.plot(x2,res_type[0] / 277, label="类型推断错误",color ='r') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
# plt.plot(x3,res_syntax[0] / 173, label="语法分析错误",color='c')
#
#
# print(res_positive[0][400]/365)
# print(res_type[0][351]/277)
# print(res_syntax[0][509]/173)
#
# plt.xlabel("bug修复时间",fontsize=16,labelpad = 6,fontproperties=prop)
# plt.ylabel("bug比例",fontsize=16,labelpad = 6,fontproperties=prop)
#
# plt.legend(loc='lower right',fontsize=16,prop=prop)
# #plt.xticks([1,100,200,300,400,500,800])
# #plt.yticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
# # 添加网格线
# plt.grid(linestyle="--", alpha=0.5)
# plt.savefig('Symptom-Bug-Fixing_Time1.png')
# print(plt.show())


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import matplotlib.font_manager as fm
plt.rc('font',family='Times New Roman')
# 设置字体为宋体
font_path = r"C:\Windows\Fonts\STSONG.ttf"
prop = fm.FontProperties(fname=font_path)

print('---------------------------------crash---------------------------------------')
df_crash=pd.read_excel('1.crash.xlsx', engine='openpyxl')
df_crash['Opened']=pd.to_datetime(df_crash['Opened'])
df_crash['Closed']=pd.to_datetime(df_crash['Closed'])
leadtime3=(df_crash['Closed'] - df_crash['Opened']).map(lambda x:x.days)
df_crash['Duration_Date']=leadtime3

crash_day_um_list=df_crash['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_crash['Duration_Date'].mean())
print('median: ', df_crash['Duration_Date'].median())
print('std: ',df_crash['Duration_Date'].std())
print('max: ',df_crash['Duration_Date'].max())
print('min: ',df_crash['Duration_Date'].min())

print('---------------------------------build---------------------------------------')
df_build=pd.read_excel('4.build error.xlsx', engine='openpyxl')
df_build['Opened']=pd.to_datetime(df_build['Opened'])
df_build['Closed']=pd.to_datetime(df_build['Closed'])
leadtime3=(df_build['Closed'] - df_build['Opened']).map(lambda x:x.days)
df_build['Duration_Date']=leadtime3

build_day_um_list=df_build['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_build['Duration_Date'].mean())
print('median: ', df_build['Duration_Date'].median())
print('std: ',df_build['Duration_Date'].std())
print('max: ',df_build['Duration_Date'].max())
print('min: ',df_build['Duration_Date'].min())

print('---------------------------------performance---------------------------------------')
df_performance=pd.read_excel('5.bad performance.xlsx', engine='openpyxl')
df_performance['Opened']=pd.to_datetime(df_performance['Opened'])
df_performance['Closed']=pd.to_datetime(df_performance['Closed'])
leadtime3=(df_performance['Closed'] - df_performance['Opened']).map(lambda x:x.days)
df_performance['Duration_Date']=leadtime3

performance_day_um_list=df_performance['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_performance['Duration_Date'].mean())
print('median: ', df_performance['Duration_Date'].median())
print('std: ',df_performance['Duration_Date'].std())
print('max: ',df_performance['Duration_Date'].max())
print('min: ',df_performance['Duration_Date'].min())

print('---------------------------------unreported---------------------------------------')
df_unreported=pd.read_excel('7.unreported.xlsx', engine='openpyxl')
df_unreported['Opened']=pd.to_datetime(df_unreported['Opened'])
df_unreported['Closed']=pd.to_datetime(df_unreported['Closed'])
leadtime3=(df_unreported['Closed'] - df_unreported['Opened']).map(lambda x:x.days)
df_unreported['Duration_Date']=leadtime3

unreported_day_um_list=df_unreported['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_unreported['Duration_Date'].mean())
print('median: ', df_unreported['Duration_Date'].median())
print('std: ',df_unreported['Duration_Date'].std())
print('max: ',df_unreported['Duration_Date'].max())
print('min: ',df_unreported['Duration_Date'].min())

print('------------------------draw picture!------------------------')
#,defaultreallimits=(1,1000) 从小于1开始算个数
res_crash=stats.cumfreq(crash_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
res_build=stats.cumfreq(build_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
res_performance=stats.cumfreq(performance_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
res_unreported=stats.cumfreq(unreported_day_um_list, numbins=1000, defaultreallimits=(0, 1000))

lowerlimit_crash=res_crash.lowerlimit
lowerlimit_build=res_build.lowerlimit
lowerlimit_performance=res_performance.lowerlimit
lowerlimit_unreported=res_unreported.lowerlimit
lowerlimit=(lowerlimit_crash+lowerlimit_build+lowerlimit_performance+lowerlimit_unreported)/4

#柱形的宽度
binsize_crash=res_crash.binsize
binsize_build=res_build.binsize
binsize_performance=res_performance.binsize
binsize_unreported=res_unreported.binsize
binsize=(binsize_crash+binsize_build+binsize_performance+binsize_unreported)/4

#柱形的高度(x中的数值有多少个会积累落入该柱形中,元素的个数)
cumcount_crash=res_crash.cumcount
cumcount_build=res_build.cumcount
cumcount_performance=res_performance.cumcount
cumcount_unreported=res_unreported.cumcount
cumcount=(cumcount_crash+cumcount_build+cumcount_performance+cumcount_unreported)/4

x1= lowerlimit_crash + np.linspace(0, binsize_crash * cumcount_crash.size, cumcount_crash.size)
x2= lowerlimit_build + np.linspace(0, binsize_build * cumcount_build.size, cumcount_build.size)
x3= lowerlimit_performance + np.linspace(0, binsize_performance * cumcount_performance.size, cumcount_performance.size)
x4= lowerlimit_unreported + np.linspace(0, binsize_unreported * cumcount_unreported.size, cumcount_unreported.size)
x=lowerlimit+np.linspace(0,binsize*cumcount.size,cumcount.size)


fig=plt.figure(figsize=(12, 8), dpi=100)

ax = fig.add_subplot(1,1,1)  #（xxx）这里前两个表示几*几的网格，最后一个表示第几子图
#plt.rcParams['font.sans-serif']='Arial'
ax.set_ylim(0, 1.01)
ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])

plt.xticks([0,100,200,259,286,400,500,583,700,800,900,1000],fontsize=14)
plt.yticks(fontsize=14)
plt.plot(x1,res_crash[0] / 112, label="崩溃",color='b') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x2,res_build[0] / 89, label="构建错误",color='r')
plt.plot(x3,res_performance[0] / 52, label="性能不佳",color='c')
plt.plot(x4,res_unreported[0] / 61, label="未知",color='m')


print(res_crash[0][286]/112)
print(res_build[0][259]/89)
print(res_performance[0][583]/52)

plt.xlabel("bug修复时间",fontsize=16,labelpad = 6,fontproperties=prop)
plt.ylabel("bug比例",fontsize=16,labelpad = 6,fontproperties=prop)

plt.legend(loc='lower right',fontsize=16,prop=prop)
#plt.xticks([1,100,200,300,400,500,800])
#plt.yticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
# 添加网格线
plt.grid(linestyle="--", alpha=0.5)
plt.savefig('Symptom-Bug-Fixing_Time2.png')
print(plt.show())