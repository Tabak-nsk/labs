# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re

def get_ip_from_cfg(file):
    with open(file, 'r') as f:
        ip_mask=[]
        dict_intf_ip_mask={}
        for line in f:
            line_intf=re.search(r'interface (\w+(?:/\d)?(\.\d+)?)',line)
            if line_intf:
                intf=line_intf.group(1)
            line_ip=re.search(r' ip address ((?:\d{1,3}\.){3}\d{1,3}) ((?:\d{1,3}\.){3}\d{1,3})',line)
            if line_ip:
                dict_temp={intf:line_ip.group(1,2)}
                dict_intf_ip_mask.update(dict_temp)
        return dict_intf_ip_mask
       
    
if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))