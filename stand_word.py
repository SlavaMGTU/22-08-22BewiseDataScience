import csv
import pandas as pd

filename = 'stand_word.csv'

greeting = ['доброе утро', 'добрый день', 'добрый вечер','здравствуйте', 'с добрым утром']
bye = ['до свидания', 'всего доброго', 'всего хорошего', 'хорошего утра', 'хорошего дня', 'хорошего вечера',
       'счастливо', 'до встречи', 'до понедельника', 'до вторника', 'до среды', 'до четверга', 'до пятницы',
       'до субботы', 'до воскресенья']
name_manager = ['ангелина'] #, ''
name_company = ['компания диджитал бизнес']

dict = {"greeting": greeting, "bye": bye, "name_manager": name_manager, "name_company": name_company}

max_len=0
for value in dict.values():
    if max_len < len(value):
        max_len = len(value)

for key, value in dict.items():
    for i in range(max_len):
        if len(value)-1 < i:
            value.append(None)
    dict[key] = value

df = pd.DataFrame(dict)

df.to_csv(filename)

