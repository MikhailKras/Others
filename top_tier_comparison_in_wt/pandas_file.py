import pandas as pd
import data_file

df = pd.DataFrame({'Nation': [x[0][0] for x in data_file.sort_dict], 'Name': [x[0][1] for x in data_file.sort_dict],
                   'Engine Power, hp': [x[1][0] for x in data_file.sort_dict], 'Weight, t': [x[1][1] for x in data_file.sort_dict],
                   'Power Density, hp/t': [x[1][2] for x in data_file.sort_dict]})
df.index += 1
max_colwidth = 0
for out_elem in data_file.sort_dict:
    for in_elem in out_elem:
        if len(str(in_elem)) > max_colwidth:
            max_colwidth = len(str(in_elem))
pd.set_option('display.max_colwidth', max_colwidth, 'display.max_columns', 5, 'display.width', len(df.columns)*max_colwidth)
with open('output_file.txt', mode='w', encoding='utf-8') as file:
    print(df, file=file)
