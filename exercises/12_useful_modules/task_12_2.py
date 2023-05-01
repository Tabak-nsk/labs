# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress

def convert_ranges_to_ip_list(ip_list):
    result_ip_list=[]
    for ip in ip_list:
        if '-' in ip:
            ip=ip.split('-')
            ip_start_range=ipaddress.ip_address(ip[0])
            if '.' in ip[1]:
                ip_end_range=ipaddress.ip_address(ip[1])
            else:
                ip_per_octets=ip[0].split('.')
                ip_per_octets.pop(3)
                ip_per_octets.insert(3,ip[1])
                ip_end_range=ipaddress.ip_address('.'.join(ip_per_octets))

            while ip_start_range <= ip_end_range:
                result_ip_list.append(str(ip_start_range))
                ip_start_range+=1
        else:
            result_ip_list.append(ip)
    return result_ip_list

if __name__ == '__main__':
    ip_list=['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(ip_list))