# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import glob
import re
import yaml

def generate_topology_from_cdp(list_of_files,save_to_filename=None):
    '''
    Функция обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую
    топологию в один словарь.
    '''
    result_dict_final={}
    for files in list_of_files:
        f = open(files, 'r')
        output_show_cdp_neighbors=f.read()
        #регулярное выражение для извлечения значений вывода
        regex = r'(\w+)\s+(\w+ \d\/\d)\s+\d+\s+\w? \w? \w?\s+\S+\s+(\w+ \d\/\d)'
        #извлекаем хостнейм
        hostname = re.search(r'(\w+)>|#',output_show_cdp_neighbors).group(1)
        #генератор словаря с извлечением совпадений из итератора
        result_dict = {hostname:{match.group(2):{match.group(1):match.group(3)} for match in re.finditer(regex,output_show_cdp_neighbors)}}
        #добавляем результаты в финальный словарь
        result_dict_final.update(result_dict)
    #если передано имя файла - записать результаты в файл
    if save_to_filename:
        with open(save_to_filename, 'w') as f_yaml:
            yaml.dump(result_dict_final, f_yaml)
    return result_dict_final

if __name__ == '__main__':
    sh_cdp_files = glob.glob("sh_cdp*")
    #print(sh_cdp_files)
    print(generate_topology_from_cdp(sh_cdp_files,'topology.yaml'))
