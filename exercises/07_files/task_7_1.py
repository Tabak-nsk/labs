# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

prefix_template="""
Prefix                {0}
AD/Metric             {1}
Next-Hop              {2}
Last update           {3}
Outbound Interface    {4}
"""

with open('ospf.txt', 'r') as f:
    for line in f:
        line=line.replace('O        ','').replace('[','').replace(']','').replace('via','').replace(',','').strip().split()
#        print(type(line))
        print(prefix_template.format(*line))