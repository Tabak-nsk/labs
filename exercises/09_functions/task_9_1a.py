# -*- coding: utf-8 -*-
"""
Задание 9.1a

Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли
настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд
   port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_mode_template и шаблона port_security_template,
если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config, с генерацией конфигурации
port-security и без.

Пример вызова функции:
print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

#print(access_config)
def generate_access_config(intf_vlan_mapping, access_template,psecurity=None):
    intf_cfg=[]
#    intf_cfg=[[f"interface {intf}  {command}" for intf,vlan in intf_vlan_mapping.items()] for command in access_template]
    for intf,vlan in intf_vlan_mapping.items():
        intf_cfg.append(f"interface {intf}")
#        print (f"interface {intf}")
        for command in access_template:
            if 'switchport access vlan' in command:
                intf_cfg.append(f"{command} {vlan}")
 #               print(f"{command} {vlan}")
            else: intf_cfg.append(f"{command}")
        if psecurity is not None:
            for command_ps in psecurity:
                intf_cfg.append(f"{command_ps}")
#    #print(access_template)
    return intf_cfg
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
#print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template,port_security_template))
#generate_access_config(access_config_2, access_mode_template)
