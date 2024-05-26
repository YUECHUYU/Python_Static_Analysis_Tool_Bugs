import pandas as pd

# 读取Excel表格
file_path = 'mypy.xlsx'  # Excel文件路径
df = pd.read_excel(file_path, engine='openpyxl')

# 根据'symptoms'列的值拆分数据
# grouped_data = df.groupby('Symptoms')
grouped_data = df.groupby('Root_Causes')

# 将每个组写入不同的Excel文件
for group_name, group_df in grouped_data:
    output_file = f'{group_name}.xlsx'
    group_df.to_excel(output_file, index=False, engine='openpyxl')
