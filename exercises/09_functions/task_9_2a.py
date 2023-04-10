# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):

    intf_cfg_dict={}
    for intf,vlans in intf_vlan_mapping.items():
        intf_cfg=[]
        #преобразуем список чисел в строку
        vlan_str=''
        if len(vlans)>1:
            for vlan in vlans:
                vlan_str=vlan_str+' '+str(vlan)
        else: vlan_str=str(vlans[0])
        vlan_str=vlan_str.strip().replace(' ',',')
        for command in trunk_template:
            if 'switchport trunk allowed vlan' in command:
                intf_cfg.append(f"{command} {str(vlan_str)}")
            else: intf_cfg.append(f"{command}")
        intf_cfg_dict[intf]=intf_cfg
    return intf_cfg_dict
print(generate_trunk_config(trunk_config, trunk_mode_template))