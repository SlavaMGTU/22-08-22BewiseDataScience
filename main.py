import numpy as np
import pandas as pd
import csv
import io

file_name = 'test_data1.csv'
f_stand_word = 'stand_word.csv'
filename_new = 'test_data1_new.csv'
filename_report = 'test_data1_report.csv'

df_stand_word = pd.read_csv(
    filepath_or_buffer = f_stand_word,
    delimiter = ',',
    encoding='utf8',
    header = 0
) # read file stand_word.csv

a=0
df_file = pd.read_csv(
    filepath_or_buffer = file_name,
    delimiter = ',',
    encoding='utf8',
    header = 0
)# read file test_data1.csv

columns_new =  ['dlg_id', 'line_n', 'role', 'text', 'insight', 'greeting', 'bye', 'name_manager', 'name_company']
file_new = []
row_new=[]

for i, row in df_file.iterrows():
    row_new = row.values.tolist()
    c=[]
    c = ['']*5
    row_new.extend(c)
    #list.insert(i, x)
    for i1, row1 in df_stand_word.iterrows():
        if row['role'] == 'client' and \
                str(row['text']).lower().find(str(row1['greeting']).lower()) != -1 and \
                row1['greeting'] != '':# greeting
            row_new[4]= str(row_new[4]) + 'greeting=True / '
            row_new[5]= str(row_new[5]) + ' / ' + row1['greeting']
            a = 1
        else:
            a = 1
        if row['role'] == 'client' and \
                str(row['text']).lower().find(str(row1['bye']).lower()) != -1 and \
                row1['bye'] != '':# bye
            row_new[4]= str(row_new[4]) + 'bye=True / '
            row_new[6]= str(row_new[6]) + ' / ' + row1['bye']
            a = 1
        else:
            a = 1
        if row['role'] == 'client' and \
                str(row['text']).lower().find(str(row1['name_manager']).lower()) != -1 and \
                row1['name_manager'] != '':  # name_manager
            row_new[4]= str(row_new[4]) + 'name_manager=True / '
            row_new[7]= str(row_new[7]) + ' / ' + row1['name_manager']
            a = 1
        else:
            a = 1
        if row['role'] == 'client' and \
                str(row['text']).lower().find(str(row1['name_company']).lower()) != -1 and \
                row1['name_company'] != '':  # name_company
            row_new[4]= str(row_new[4]) + 'name_company=True / '
            row_new[8]= str(row_new[8]) + ' / ' + row1['name_company']
            a = 1
        else:
            a = 1
    file_new.append(row_new)

#df = pd.DataFrame(file_new).T
a = 1
np_arr = np.array(file_new)
df = pd.DataFrame(data=np_arr, columns=columns_new)

df.to_csv(filename_new, index = False, sep=',', encoding='utf-8')# columns=columns_new )
