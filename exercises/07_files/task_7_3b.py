# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
mac_input=input('Веедите мак:')
with open('CAM_table.txt', 'r') as file_src:
    macs=list('')
#    print(type(mac))
    for line in file_src:
        if 'DYNAMIC' in line:
            mac=line.strip().replace('DYNAMIC','').split()
            if mac[0]==mac_input:
                mac[0]=int(mac[0])
                macs.append(mac)
    macs.sort()
#    print(macs)
    #macs=','.join(macs)
    for mac in macs:
        vlan,macc,port=mac
        print("{:<9} {:<20} {:<6}".format(vlan,macc,port))