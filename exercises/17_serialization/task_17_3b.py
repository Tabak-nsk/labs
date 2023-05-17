# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий
для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно,
чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии,
но и удалять "дублирующиеся" соединения (их лучше всего видно на схеме, которую
генерирует функция draw_topology из файла draw_network_graph.py).
Тут "дублирующиеся" соединения, это ситуация когда в словаре есть два соединения:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Из-за того что один и тот же линк описывается дважды, на схеме будут лишние соединения.
Задача оставить только один из этих линков в итоговом словаре, не важно какой.

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии
с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть "дублирующихся" линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
import yaml, draw_network_graph

def unique_dict_keys_values(topology_dict):
    '''
    Функция которая на входе ожидает словарь и проверяет уникальность ключей и значений
    На выходе возвращает словарь где ключи и значения уникальны
    '''
    topology_dict2 = topology_dict.copy()
#    print(topology_dict)
    for key in topology_dict2.keys():
        topology_dict2 = topology_dict.copy()
        for value in topology_dict2.values():
#            print(position,key,value)
            if key==value:
                del topology_dict[key]
#                print(topology_dict)
    return topology_dict

def transform_topology(topology_file_yaml):
    '''
    Функция на входе ожидает имя yaml файла
    Cчитывает его и преобразует в словарь кортежей
    '''
    topology_dict_final={}
    with open(topology_file_yaml) as f:
        from_yaml = yaml.safe_load(f)
    #print(from_yaml)
    for host,neighbor_data in from_yaml.items():
        #print(host,neighbor_data)
        for host_intf,neighbor in neighbor_data.items():
            #print(host_intf,neighbor)
            for nbr_host,nbr_intf in neighbor.items():
                topology_dict = {(host,host_intf):(nbr_host,nbr_intf)}
            topology_dict_final.update(topology_dict)
    #print (unique_network_map(topology_dict_final))
    #print(topology_dict_final)
    return unique_dict_keys_values(topology_dict_final)
    
if __name__ == '__main__':
    #transform_topology('topology.yaml')
    #print(unique_network_map(transform_topology('topology.yaml')))
    draw_network_graph.draw_topology(transform_topology('topology.yaml'))
    
    
    
