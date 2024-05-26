import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import matplotlib.font_manager as fm
plt.rc('font',family='Times New Roman')
# 设置字体为宋体
font_path = r"C:\Windows\Fonts\STSONG.ttf"
prop = fm.FontProperties(fname=font_path)

print('---------------------------------algo---------------------------------------')
df_algo=pd.read_excel('1.algorithm.xlsx', engine='openpyxl')
df_algo['Opened']=pd.to_datetime(df_algo['Opened'])
df_algo['Closed']=pd.to_datetime(df_algo['Closed'])
leadtime3=(df_algo['Closed'] - df_algo['Opened']).map(lambda x:x.days)
df_algo['Duration_Date']=leadtime3

algo_day_um_list=df_algo['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_algo['Duration_Date'].mean())
print('median: ', df_algo['Duration_Date'].median())
print('std: ',df_algo['Duration_Date'].std())
print('max: ',df_algo['Duration_Date'].max())
print('min: ',df_algo['Duration_Date'].min())

print('---------------------------------exception---------------------------------------')
df_exception=pd.read_excel('3.exception.xlsx', engine='openpyxl')

df_exception['Opened']=pd.to_datetime(df_exception['Opened'])
df_exception['Closed']=pd.to_datetime(df_exception['Closed'])
leadtime3=(df_exception['Closed'] - df_exception['Opened']).map(lambda x:x.days)
df_exception['Duration_Date']=leadtime3
exception_day_um_list=df_exception['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_exception['Duration_Date'].mean())
print('median: ', df_exception['Duration_Date'].median())
print('std: ',df_exception['Duration_Date'].std())
print('max: ',df_exception['Duration_Date'].max())
print('min: ',df_exception['Duration_Date'].min())

print('---------------------------------config---------------------------------------')
df_config=pd.read_excel('7.config.xlsx', engine='openpyxl')
df_config['Opened']=pd.to_datetime(df_config['Opened'])
df_config['Closed']=pd.to_datetime(df_config['Closed'])
leadtime3=(df_config['Closed'] - df_config['Opened']).map(lambda x:x.days)
df_config['Duration_Date']=leadtime3

config_day_um_list=df_config['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_config['Duration_Date'].mean())
print('median: ', df_config['Duration_Date'].median())
print('std: ',df_config['Duration_Date'].std())
print('max: ',df_config['Duration_Date'].max())
print('min: ',df_config['Duration_Date'].min())

print('---------------------------------condition---------------------------------------')
df_condition=pd.read_excel('5.condition.xlsx', engine='openpyxl')
df_condition['Opened']=pd.to_datetime(df_condition['Opened'])
df_condition['Closed']=pd.to_datetime(df_condition['Closed'])
leadtime3=(df_condition['Closed'] - df_condition['Opened']).map(lambda x:x.days)
df_condition['Duration_Date']=leadtime3

condition_day_um_list=df_condition['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_condition['Duration_Date'].mean())
print('median: ', df_condition['Duration_Date'].median())
print('std: ',df_condition['Duration_Date'].std())
print('max: ',df_condition['Duration_Date'].max())
print('min: ',df_condition['Duration_Date'].min())

print('---------------------------------assi---------------------------------------')
df_assi=pd.read_excel('6.assi.xlsx', engine='openpyxl')
df_assi['Opened']=pd.to_datetime(df_assi['Opened'])
df_assi['Closed']=pd.to_datetime(df_assi['Closed'])
leadtime3=(df_assi['Closed'] - df_assi['Opened']).map(lambda x:x.days)
df_assi['Duration_Date']=leadtime3

assi_day_um_list=df_assi['Duration_Date'].values.tolist()

print('Duration_Date:  ')
print('mean: ', df_assi['Duration_Date'].mean())
print('median: ', df_assi['Duration_Date'].median())
print('std: ',df_assi['Duration_Date'].std())
print('max: ',df_assi['Duration_Date'].max())
print('min: ',df_assi['Duration_Date'].min())

print('------------------------draw picture!------------------------')
#,defaultreallimits=(1,1000) 从小于1开始算个数
res_algo=stats.cumfreq(algo_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
res_exception=stats.cumfreq(exception_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
res_config=stats.cumfreq(config_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
res_condition=stats.cumfreq(condition_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
res_assi=stats.cumfreq(assi_day_um_list, numbins=1000, defaultreallimits=(0, 1000))

lowerlimit_algo=res_algo.lowerlimit
lowerlimit_exception=res_exception.lowerlimit
lowerlimit_config=res_config.lowerlimit
lowerlimit_condition=res_condition.lowerlimit
lowerlimit_assi=res_assi.lowerlimit
lowerlimit=(lowerlimit_exception+lowerlimit_algo+lowerlimit_config+lowerlimit_condition+lowerlimit_assi)/5

#柱形的宽度
binsize_algo=res_algo.binsize
binsize_exception=res_exception.binsize
binsize_config=res_config.binsize
binsize_condition=res_condition.binsize
binsize_assi=res_assi.binsize
binsize=(binsize_exception+binsize_algo+binsize_config+binsize_condition+binsize_assi)/5

#柱形的高度(x中的数值有多少个会积累落入该柱形中,元素的个数)
cumcount_algo=res_algo.cumcount
cumcount_exception=res_exception.cumcount
cumcount_config=res_config.cumcount
cumcount_condition=res_condition.cumcount
cumcount_assi=res_assi.cumcount
cumcount=(cumcount_exception+cumcount_algo+cumcount_config+cumcount_condition+cumcount_assi)/5

x1= lowerlimit_algo + np.linspace(0, binsize_algo * cumcount_algo.size, cumcount_algo.size)
x2=lowerlimit_exception+np.linspace(0,binsize_exception*cumcount_exception.size,cumcount_exception.size)
x3= lowerlimit_config + np.linspace(0, binsize_config * cumcount_config.size, cumcount_config.size)
x4= lowerlimit_condition + np.linspace(0, binsize_condition * cumcount_condition.size, cumcount_condition.size)
x5= lowerlimit_assi + np.linspace(0, binsize_assi * cumcount_assi.size, cumcount_assi.size)
x=lowerlimit+np.linspace(0,binsize*cumcount.size,cumcount.size)


fig=plt.figure(figsize=(12, 8), dpi=100)

ax = fig.add_subplot(1,1,1)  #（xxx）这里前两个表示几*几的网格，最后一个表示第几子图
#plt.rcParams['font.sans-serif']='Arial'
ax.set_ylim(0, 1.01)
ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])

plt.xticks([0,100,200,300,385,509,562,600,700,732,835,900,1000],fontsize=14)
plt.yticks(fontsize=14)
plt.plot(x1,res_algo[0] / 440, label="错误的算法实施",color='b') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x2,res_exception[0] / 209, label="异常处理不当",color ='r') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x3,res_config[0] / 156, label="错误的配置",color='c')
plt.plot(x4,res_condition[0] / 108, label="错误的条件逻辑",color='m')
plt.plot(x5,res_assi[0] / 58, label="错误的赋值",color='y')

print(res_algo[0][732]/440)
print(res_exception[0][835]/209)
print(res_config[0][509]/156)
print(res_condition[0][385]/108)
print(res_assi[0][562]/58)

plt.xlabel("bug修复时间",fontsize=16,labelpad = 6,fontproperties=prop)
plt.ylabel("bug比例",fontsize=16,labelpad = 6,fontproperties=prop)

plt.legend(loc='lower right',fontsize=16,prop=prop)
#plt.xticks([1,100,200,300,400,500,800])
#plt.yticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
# 添加网格线
plt.grid(linestyle="--", alpha=0.5)
plt.savefig('Root-Bug-Fixing_Time1.png')
print(plt.show())


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
# print('---------------------------------checks---------------------------------------')
# df_checks=pd.read_excel('8.checks.xlsx', engine='openpyxl')
# df_checks['Opened']=pd.to_datetime(df_checks['Opened'])
# df_checks['Closed']=pd.to_datetime(df_checks['Closed'])
# leadtime3=(df_checks['Closed'] - df_checks['Opened']).map(lambda x:x.days)
# df_checks['Duration_Date']=leadtime3
#
# checks_day_um_list=df_checks['Duration_Date'].values.tolist()
#
# print('Duration_Date:  ')
# print('mean: ', df_checks['Duration_Date'].mean())
# print('median: ', df_checks['Duration_Date'].median())
# print('std: ',df_checks['Duration_Date'].std())
# print('max: ',df_checks['Duration_Date'].max())
# print('min: ',df_checks['Duration_Date'].min())
#
# print('---------------------------------envir---------------------------------------')
# df_envir=pd.read_excel('10.envir.xlsx', engine='openpyxl')
#
# df_envir['Opened']=pd.to_datetime(df_envir['Opened'])
# df_envir['Closed']=pd.to_datetime(df_envir['Closed'])
# leadtime3=(df_envir['Closed'] - df_envir['Opened']).map(lambda x:x.days)
# df_envir['Duration_Date']=leadtime3
# envir_day_um_list=df_envir['Duration_Date'].values.tolist()
#
# print('Duration_Date:  ')
# print('mean: ', df_envir['Duration_Date'].mean())
# print('median: ', df_envir['Duration_Date'].median())
# print('std: ',df_envir['Duration_Date'].std())
# print('max: ',df_envir['Duration_Date'].max())
# print('min: ',df_envir['Duration_Date'].min())
#
# print('---------------------------------memory---------------------------------------')
# df_memory=pd.read_excel('2.memory.xlsx', engine='openpyxl')
# df_memory['Opened']=pd.to_datetime(df_memory['Opened'])
# df_memory['Closed']=pd.to_datetime(df_memory['Closed'])
# leadtime3=(df_memory['Closed'] - df_memory['Opened']).map(lambda x:x.days)
# df_memory['Duration_Date']=leadtime3
#
# memory_day_um_list=df_memory['Duration_Date'].values.tolist()
#
# print('Duration_Date:  ')
# print('mean: ', df_memory['Duration_Date'].mean())
# print('median: ', df_memory['Duration_Date'].median())
# print('std: ',df_memory['Duration_Date'].std())
# print('max: ',df_memory['Duration_Date'].max())
# print('min: ',df_memory['Duration_Date'].min())
#
# print('---------------------------------concurrency---------------------------------------')
# df_concurrency=pd.read_excel('9.concurrency.xlsx', engine='openpyxl')
# df_concurrency['Opened']=pd.to_datetime(df_concurrency['Opened'])
# df_concurrency['Closed']=pd.to_datetime(df_concurrency['Closed'])
# leadtime3=(df_concurrency['Closed'] - df_concurrency['Opened']).map(lambda x:x.days)
# df_concurrency['Duration_Date']=leadtime3
#
# concurrency_day_um_list=df_concurrency['Duration_Date'].values.tolist()
#
# print('Duration_Date:  ')
# print('mean: ', df_concurrency['Duration_Date'].mean())
# print('median: ', df_concurrency['Duration_Date'].median())
# print('std: ',df_concurrency['Duration_Date'].std())
# print('max: ',df_concurrency['Duration_Date'].max())
# print('min: ',df_concurrency['Duration_Date'].min())
#
# print('---------------------------------others---------------------------------------')
# df_others=pd.read_excel('11.others.xlsx', engine='openpyxl')
# df_others['Opened']=pd.to_datetime(df_others['Opened'])
# df_others['Closed']=pd.to_datetime(df_others['Closed'])
# leadtime3=(df_others['Closed'] - df_others['Opened']).map(lambda x:x.days)
# df_others['Duration_Date']=leadtime3
#
# others_day_um_list=df_others['Duration_Date'].values.tolist()
#
# print('Duration_Date:  ')
# print('mean: ', df_others['Duration_Date'].mean())
# print('median: ', df_others['Duration_Date'].median())
# print('std: ',df_others['Duration_Date'].std())
# print('max: ',df_others['Duration_Date'].max())
# print('min: ',df_others['Duration_Date'].min())
#
# print('------------------------draw picture!------------------------')
# #,defaultreallimits=(1,1000) 从小于1开始算个数
# res_checks=stats.cumfreq(checks_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
# res_envir=stats.cumfreq(envir_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
# res_memory=stats.cumfreq(memory_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
# res_concurrency=stats.cumfreq(concurrency_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
# res_others=stats.cumfreq(others_day_um_list, numbins=1000, defaultreallimits=(0, 1000))
#
# lowerlimit_checks=res_checks.lowerlimit
# lowerlimit_envir=res_envir.lowerlimit
# lowerlimit_memory=res_memory.lowerlimit
# lowerlimit_concurrency=res_concurrency.lowerlimit
# lowerlimit_others=res_others.lowerlimit
# lowerlimit=(lowerlimit_envir+lowerlimit_checks+lowerlimit_memory+lowerlimit_concurrency+lowerlimit_others)/5
#
# #柱形的宽度
# binsize_checks=res_checks.binsize
# binsize_envir=res_envir.binsize
# binsize_memory=res_memory.binsize
# binsize_concurrency=res_concurrency.binsize
# binsize_others=res_others.binsize
# binsize=(binsize_envir+binsize_checks+binsize_memory+binsize_concurrency+binsize_others)/5
#
# #柱形的高度(x中的数值有多少个会积累落入该柱形中,元素的个数)
# cumcount_checks=res_checks.cumcount
# cumcount_envir=res_envir.cumcount
# cumcount_memory=res_memory.cumcount
# cumcount_concurrency=res_concurrency.cumcount
# cumcount_others=res_others.cumcount
# cumcount=(cumcount_envir+cumcount_checks+cumcount_memory+cumcount_concurrency+cumcount_others)/5
#
# x1= lowerlimit_checks + np.linspace(0, binsize_checks * cumcount_checks.size, cumcount_checks.size)
# x2=lowerlimit_envir+np.linspace(0,binsize_envir*cumcount_envir.size,cumcount_envir.size)
# x3= lowerlimit_memory + np.linspace(0, binsize_memory * cumcount_memory.size, cumcount_memory.size)
# x4= lowerlimit_concurrency + np.linspace(0, binsize_concurrency * cumcount_concurrency.size, cumcount_concurrency.size)
# x5= lowerlimit_others + np.linspace(0, binsize_others * cumcount_others.size, cumcount_others.size)
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
# plt.xticks([0,100,220,300,400,500,541,600,700,772,900,1000],fontsize=14)
# plt.yticks(fontsize=14)
# plt.plot(x1,res_checks[0] / 51, label="缺失条件检查",color='b') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
# plt.plot(x2,res_envir[0] / 23, label="环境不兼容",color ='r') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
# plt.plot(x3,res_memory[0] / 22, label="内存",color='c')
# plt.plot(x4,res_concurrency[0] / 10, label="并发",color='m')
# plt.plot(x5,res_others[0] / 52, label="其他",color='y')
#
# print(res_checks[0][772]/51)
# print(res_envir[0][541]/23)
# print(res_memory[0][220]/22)
# print(res_concurrency[0][220]/10)
#
# plt.xlabel("bug修复时间",fontsize=16,labelpad = 6,fontproperties=prop)
# plt.ylabel("bug比例",fontsize=16,labelpad = 6,fontproperties=prop)
#
# plt.legend(loc='lower right',fontsize=16,prop=prop)
# #plt.xticks([1,100,200,300,400,500,800])
# #plt.yticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
# # 添加网格线
# plt.grid(linestyle="--", alpha=0.5)
# plt.savefig('Root-Bug-Fixing_Time2.png')
# print(plt.show())