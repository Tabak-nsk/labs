# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



ip_correct = False

while not ip_correct:
    ip=input('Введите ip:')
    ip=ip.split('.')
    if len(ip)!=4:
        print("неправильный ip-адрес")
    elif not ip[0].isdigit() or not ip[0].isdigit() or not ip[2].isdigit() or not ip[3].isdigit():
        print("неправильный ip-адрес")
    elif int(ip[0]) < 0 or int(ip[0]) > 255 or int(ip[1]) < 0 or int(ip[1]) > 255 or int(ip[2]) < 0 or int(ip[2]) > 255 or int(ip[3]) < 0 or int(ip[3]) > 255:
        print("неправильный ip-адрес")
    else:
        ip_correct = True

if int(ip[0]) >= 1 and int(ip[0]) <= 223:
    print('unicast')
elif int(ip[0]) >= 224 and int(ip[0]) <= 239:
    print('multicast')
elif int(ip[0]) == 255 and int(ip[1]) == 255 and int(ip[2]) == 255 and int(ip[3]) == 255:
    print('local broadcast')
elif int(ip[0]) == 0 and int(ip[1]) == 0 and int(ip[2]) == 0 and int(ip[3]) == 0:
    print('unassigned')
else:
    print('unused')