# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import csv
import re

def  write_dhcp_snooping_to_csv(filenames,output):
    
    headers=['switch','mac','ip','vlan','interface']
    #открываем csv файл на запись
    with open(output, 'w') as file_output:
        writer = csv.writer(file_output)
        #записываем заголовок
        writer.writerow(headers)
        #print(headers)
        for filename in filenames:
            #извлекаем хостнейм из имени файла
            match=re.match(r'(^\w+)_\w+_\w+',filename)
            hostname=match.group(1)
            #print(headers)
            with open(filename, 'r') as f:
                for line in f:
                    #извлекаем информацию для записи в файл
                    match=re.search(r'((?:\w{2}:){5}\w{2})\s+'
                                    r'((?:\d{1,3}.){3}\d{1,3})\s+\d+\s+dhcp-snooping\s+'
                                    r'(\d+)\s+'
                                    r'(\w+\/?(?:\d+)?)',line)
                    #если совпадение найдено - записываем в файлы
                    if match:
                        line_output=[hostname,match.group(1),match.group(2),match.group(3),match.group(4)]
                        #print(line_output)
                        writer.writerow(line_output)
    
if __name__ == '__main__':
    filenames=['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    output='result_17.1.csv'
    write_dhcp_snooping_to_csv(filenames,output)