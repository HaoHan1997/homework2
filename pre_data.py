# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

csv_file = pd.read_csv(r"/Users/jessiechu/Documents/文档/DMPro/hw1/Data/Building_Permits.csv", low_memory=False)


column_usable = ['Permit Type', 'Permit Type Definition', 'Plansets', 'TIDF Compliance', 'Existing Construction Type', 'Proposed Construction Type']
# 格式化属性名称
column_name = []

for column in column_usable:
    column =  column.replace(' ','_')
 
    column_name.append(column)

#print(column_name)

data = csv_file[column_usable]
trans_dict = {}
record_num = data.index.__len__()
for column in column_usable:
    new_line = [""]*record_num
    for index in data.index:
        item = data[column][index]
        try:
            if np.isnan(item):
                new_line[index] = ""
            else:
                # 拼接属性和属性值
                new_line[index] = column_name[column_usable.index(column)] + "_"+ str(item).replace(' ','_')
        except BaseException as e:
            new_line[index] = column_name[column_usable.index(column)] + "_" + str(item).replace(' ','_')
    trans_dict[column] = new_line

csv_write = pd.DataFrame(trans_dict)
csv_write.to_csv('results/after_procces.csv', index=False, header=False)