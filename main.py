import numpy as np
import pandas as pd


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

lab_bool = [False, False, False, False]

for i, row in df_file.iterrows():
    row_new = row.values.tolist()
    c=[]
    c = ['']*5
    row_new.extend(c)
    for i1, row1 in df_stand_word.iterrows():
        if row['role'] == 'client' and \
                str(row['text']).lower().find(str(row1['greeting']).lower()) != -1 and \
                row1['greeting'] != '':# greeting
            row_new[4]= str(row_new[4]) + 'greeting=True / '
            row_new[5]= str(row_new[5]) + ' / ' + row1['greeting']
            lab_bool[0] = True

        if row['role'] == 'client' and \
                str(row['text']).lower().find(str(row1['bye']).lower()) != -1 and \
                row1['bye'] != '':# bye
            row_new[4]= str(row_new[4]) + 'bye=True / '
            row_new[6]= str(row_new[6]) + ' / ' + row1['bye']
            lab_bool[1] = True

        if row['role'] == 'client' and \
                str(row['text']).lower().find(str(row1['name_manager']).lower()) != -1 and \
                row1['name_manager'] != '':  # name_manager
            row_new[4]= str(row_new[4]) + 'name_manager=True / '
            row_new[7]= str(row_new[7]) + ' / ' + row1['name_manager']
            lab_bool[2] = True

        if row['role'] == 'client' and \
                str(row['text']).lower().find(str(row1['name_company']).lower()) != -1 and \
                row1['name_company'] != '':  # name_company
            row_new[4]= str(row_new[4]) + 'name_company=True / '
            row_new[8]= str(row_new[8]) + ' / ' + row1['name_company']
            lab_bool[3] = True

    if i == len(df_file)-1:
        i2 = 5
        for lab in lab_bool:
            row_new[4] = str(row_new[4]) + columns_new[i2] + '=' + str(lab) + ' / '
            i2 += 1
        lab_bool = [False, False, False, False]

    elif df_file.at[i+1,'dlg_id'] != row['dlg_id']:
        i2 = 5
        for lab in lab_bool:
            row_new[4] = str(row_new[4]) + columns_new[i2] + '=' + str(lab) + ' / '
            i2 += 1
        lab_bool = [False, False, False, False]
    list_new = row_new[4].split(' / ')
    list_new = list(set(list_new))
    row_new[4] = ' / '.join(list_new)

    file_new.append(row_new)

a = 1
np_arr = np.array(file_new)
df = pd.DataFrame(data=np_arr, columns=columns_new)
df.to_csv(filename_new, index = False, sep=',', encoding='utf-8')
