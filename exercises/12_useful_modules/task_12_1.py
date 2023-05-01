# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(ip_addresses):
    """
    Функция ping_ip_addresses, проверяет пингуются ли IP-адреса.
    Функция ожидает как аргумент список IP-адресов.
    Функция должна возвращать кортеж с двумя списками:
    * список доступных IP-адресов
    * список недоступных IP-адресов
    """
    avail_ip=[]
    unavail_ip=[]
    for ip_address in ip_addresses:
        reply= subprocess.run(['ping', '-c', '3', '-n', ip_address])
        if reply.returncode == 0:
            avail_ip.append(ip_address)
        else:
            unavail_ip.append(ip_address)
    result=(avail_ip,unavail_ip)
    return result

if __name__ == '__main__':
    ip_addresses=['8.8.8.8','1.1.1.1','a']
    print(ping_ip_addresses(ip_addresses))