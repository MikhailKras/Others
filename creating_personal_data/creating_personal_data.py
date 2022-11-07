import pandas as pd
import os
sheet = pd.read_excel('db_to.xlsx')
set_names = set()

if not os.path.isfile('names'):
    with open('names', mode='w', encoding='utf-8') as file:
        for surname in sheet['name']:
            if surname not in set_names and len(surname.split()) == 1:
                surname = surname.title().strip()
                set_names.add(surname)
                file.write(f'{surname}\n')

if not os.path.isfile('surnames'):
    with open('surnames', mode='w', encoding='utf-8') as file:
        for surname in sheet['surname']:
            if surname not in set_names and len(surname.split()) == 1:
                surname = surname.title().strip()
                set_names.add(surname)
                file.write(f'{surname}\n')
