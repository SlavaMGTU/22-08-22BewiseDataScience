# 22-08-22BewiseDataScience
Decoding and clarification of the transcript of the calls\
Имеем предварительный CSV-файл с расшифровками переговоров\
<img src="https://ibb.co/GJrr25y"><img src="https://i.ibb.co/7z00W1P/01-transcript-of-the-calls.jpg" alt="01-transcript-of-the-calls" alt="transcript-of-the-calls">
\
PY-файл "stand_word.py"  создает словарь:"stand_word.csv" содержащий стандартные фразы по категориям:\
1.greeting,\
2.bye,\
3.name_manager,\
4.name_company\
<img src="https://ibb.co/jkGKSzM"><img src="https://i.ibb.co/PG4pdMh/02-dictionary-of-expressions.jpg" alt="01-transcript-of-the-calls" alt="dictionary-of-expressions">
\
PY-файл "main.py"  создает итоговый файл:"test_data1_new.csv" с дополнительными столбцами:\
5.insight- при наличии фразы в строке - указывается тип фразы, при окончании беседы перечисляются все указанные "True" и не указанные фразы "False",\
6.greeting,\
7.bye,\
8.name_manager,\
9.name_company\
в 6-9 столбцах указываются стандартные фразы использованные в разговоре .\
<img src="https://ibb.co/m4VMdtW"><img src="https://i.ibb.co/QM31hnw/03-file-finish.jpg" alt="01-transcript-of-the-calls" alt="file-finish">
