# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
vlans_quest=dict(access='Введите номер VLAN:',trunk='Введите разрешенные VLANы:')

if_config=dict(access=access_template, trunk=trunk_template)
mode=input('Введите режим работы интерфейса (access/trunk):')
#mode='trunk'
interface=input('Введите тип и номер интерфейса:')
#interface='Fa0/1'
vlan=input(vlans_quest[mode])
#vlan='2,3'
if_config_str='\n'.join(if_config[mode])
print("interface {}".format(interface))
print(if_config_str.format(vlan))
#print(if_config[mode])