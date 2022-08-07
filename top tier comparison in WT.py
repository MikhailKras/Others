def gen_dict(country: str, name_list: list, param_list: list) -> dict:
    return {name: param for name, param in
            zip(tuple(zip((country for _ in range(len(name_list))), name_list)), list(map(lambda x, y: (x, y, round(x/y, 2)),
                                    [hp[0] for hp in param_list], [weight[1] for weight in param_list])))}


# def column_name(name_col: str, index1: int, index2:int, lst: list, last=False) -> str:
#     if last:
#         return name_col
#     return name_col + ''.join([' ' for _ in range(max([len(str(x)) for x in list(map(lambda elem: elem[index1][index2], lst))]) - len(name_col))])


britain_names = ['Challenger 2 (2F)', 'Challenger 2 TES', 'Black Night']
britain_params = [(1217, 62.5), (1217, 74.8), (1217, 62.5)]
britain_dict = gen_dict('Britain', britain_names, britain_params)

usa_names = ['M1A2 Abrams']
usa_params = [(1519, 61.7)]
usa_dict = gen_dict('USA', usa_names, usa_params)

ussr_names = ['Т-80БВМ']
ussr_params = [(1250, 46.0)]
ussr_dict = gen_dict('USSR', ussr_names, ussr_params)

japan_names = ['Type 10']
japan_params = [(1200, 44.4)]
japan_dict = gen_dict('Japan', japan_names, japan_params)

france_names = ['Leclerc', 'Leclerc S2', 'Leclerc SXXI']
france_params = [(1474, 53.7), (1474, 56.2), (1474, 56.2)]
france_dict = gen_dict('France', france_names, france_params)

germany_names = ['Leopard 2A5', 'Leopard 2A6']
germany_params = [(1500, 59.5), (1500, 60.1)]
germany_dict = gen_dict('Germany', germany_names, germany_params)

china_names = ['ZTZ99A']
china_params = [(1500, 55.0)]
china_dict = gen_dict('China', china_names, china_params)

sweden_names = ['Strv 122A', 'Strv 122B PLSS']
sweden_params = [(1500, 62.5), (1500, 62.5)]
sweden_dict = gen_dict('Sweden', sweden_names, sweden_params)

israel_names = ['Merkava Mk.4B', 'Merkava Mk.4M']
israel_params = [(1500, 65.0), (1500, 65.5)]
israel_dict = gen_dict('Israel', israel_names, israel_params)

# print(britain_dict, ussr_dict, ussr_dict, japan_dict, france_dict, germany_dict, china_dict, sweden_dict, israel_dict,
#       sep='\n')

merge_dict = {**britain_dict, **usa_dict, **ussr_dict, **japan_dict, **france_dict, **germany_dict, **china_dict,
              **sweden_dict, **israel_dict}
sort_dict = sorted(merge_dict.items(), key=lambda x: x[-1][-1], reverse=True)

with open('top tier comparison in WT.txt', mode='w', encoding='utf-8') as file:
    for place, tank in enumerate(sort_dict):
        print(f'{place+1} Country: {tank[0][0]}, Name: {tank[0][-1]}, Engine Power: {tank[-1][0]} hp, Weight: {tank[-1][1]} tonnes, '
              f'Power Density: {tank[-1][-1]} hp/t', file=file)

# with open('top tier comparison in WT.txt', mode='w', encoding='utf-8') as file:
#     name_columns_list  = [('Country', (0, 0)), ('Name', (0, 1)), ('Engine Power', (1, 0)), ('Weight', (1, 1)), ('Power Density', (1, 2))]
#     name_columns_string = '  '
#     for name_column, indexes in name_columns_list:
#         name_columns_string += column_name(name_column, indexes[0], indexes[1], sort_dict)
#     print(name_columns_string, file=file)
#     for place, tank in enumerate(sort_dict):
#         print(f'{place} {tank[0][0]} {tank[0][-1]} {tank[-1][0]} {tank[-1][1]} '
#               f'{tank[-1][-1]}', file=file)
