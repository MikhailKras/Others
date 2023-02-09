import pandas as pd

file_path = 'C:/Users/MIKHAIL/Desktop/Insta.xlsx'

sheet = pd.read_excel(f'{file_path}')
urls = sheet['Column'].tolist()
nicknames = []
for url in urls:
    split_url = url.split('?')
    split_url = split_url[0].split('/')
    nicknames.append(split_url[-1])
writer = pd.ExcelWriter(f'{file_path}')
df_nicknames = pd.DataFrame(nicknames)
df_nicknames.to_excel(writer, 'sheet1')
writer.save()
