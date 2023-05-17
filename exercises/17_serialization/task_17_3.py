# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re

def parse_sh_cdp_neighbors(output_show_cdp_neighbors):
    '''
    Функция, ожидающая на вход строку с выводом и возращающая словарь
    '''
    #регулярное выражение для извлечения значений вывода
    regex=r'(\w+)\s+(\w+ \d\/\d)\s+\d+\s+\w \w \w\s+\S+\s+(\w+ \d\/\d)'
    #извлекаем хостнейм
    hostname=re.search(r'(\w+)>|#',output_show_cdp_neighbors).group(1)
    #генератор словаря с извлечением совпадений из итератора
    result_dict={hostname:{match.group(2):{match.group(1):match.group(3)} for match in re.finditer(regex,output_show_cdp_neighbors)}}
    ##print(result_dict)
    return result_dict
    
if __name__ == '__main__':
    f = open('sh_cdp_n_sw1.txt', 'r')
    print(parse_sh_cdp_neighbors(f.read()))