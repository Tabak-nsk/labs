# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv

with open(argv[1], 'r') as f:
#with open('config_sw1.txt', 'r') as f:
    for line in f:
        if not line.startswith('!'):
            i=0
            for ignores in ignore:
                if ignores not in line:
                    i+=1
                    if i==3:
                        print(line.rstrip())