# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv

with open(argv[1], 'r') as file_src, open(argv[2], 'w') as file_dest:
#with open('config_sw1.txt', 'r') as file_src:
    for line in file_src:
        if not line.startswith('!'):
            i=0
            for ignores in ignore:
                if ignores not in line:
                    i+=1
                    if i==len(ignore):
                        file_dest.write(line)
#                        print(line.rstrip())