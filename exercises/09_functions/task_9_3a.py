# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    intf_acc_dict={}
    intf_trunk_dict={}
    line_acc=''
    with open(config_filename, 'r') as f:
        for line in f:
            if 'interface F' in line:
                intf=line.strip().replace('interface ','')
#                print(line)
            elif 'access vlan' in line:
#               print(line)
                vlans=line.strip().replace('switchport access vlan ','')
                intf_acc_dict[intf]=int(vlans)
                line_acc=''
            elif 'trunk allowed' in line:
#                    print(line)
                vlans=line.strip().replace('switchport trunk allowed vlan ','').split(',')
                vlan_digit=[]
                for vlan in vlans:
                    vlan_digit.append(int(vlan))
                intf_trunk_dict[intf]=vlan_digit
            elif 'switchport mode access' in line:
                line_acc=line_acc+line
            elif 'duplex auto' in line:
                line_acc=line_acc+line
                if 'switchport mode access\n duplex auto' in line_acc:
                    intf_acc_dict[intf]=1;
                line_acc=''
    intf_tuple=(intf_acc_dict, intf_trunk_dict)
    return intf_tuple
#    print(intf_acc_dict, intf_trunk_dict)
print(get_int_vlan_map('config_sw2.txt'))