# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    intf_acc_dict={}
    intf_trunk_dict={}
    with open(config_filename, 'r') as f:
        for line in f:
            if 'interface F' in line:
                intf=line.strip().replace('interface ','')
#                print(line)
            if 'access vlan' in line:
#                    print(line)
                    vlans=line.strip().replace('switchport access vlan ','')
                    intf_acc_dict[intf]=int(vlans)
            if 'trunk allowed' in line:
#                    print(line)
                    vlans=line.strip().replace('switchport trunk allowed vlan ','').split(',')
                    vlan_digit=[]
                    for vlan in vlans:
                        vlan_digit.append(int(vlan))
                    intf_trunk_dict[intf]=vlan_digit
    intf_tuple=(intf_acc_dict, intf_trunk_dict)
    return intf_tuple
#    print(intf_acc_dict, intf_trunk_dict)
print(get_int_vlan_map('config_sw1.txt'))