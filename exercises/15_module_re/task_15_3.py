# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re

def convert_ios_nat_to_asa(file_nat_ios,file_nat_asa):
    template_nat_asa='''object network LOCAL_{1}
 host {1}
 nat (inside,outside) static interface service {0} {2} {3}'''
    
    f_asa = open(file_nat_asa, 'w')
    with open(file_nat_ios,'r') as f_ios:
        for line in f_ios:
            #print(line)
            nat_rule=re.search(r'(tcp|udp) '
                               r'([\d.]+) '
                               r'(\d+) '
                               r'\w+ \S+ '
                               r'(\d+)'
                               ,line)
            if nat_rule:
                #nat=nat_rule.groups()
                #print(nat)
                #print(nat_rule.groupdict())
                #print(template_nat_asa.format(*nat_rule.groupdict().items()))
                print(template_nat_asa.format(*nat_rule.groups()),file=f_asa)
    f_asa.close()
    
if __name__ == '__main__':
    convert_ios_nat_to_asa('cisco_nat_config.txt','asa_nat_config.txt')