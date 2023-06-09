# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_template = '''
Network:
{0:<9} {1:<9} {2:<9} {3:<9}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
mask_template = '''
Mask:
/{4}
{0:<9} {1:<9} {2:<9} {3:<9}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
prefix=input('Введите префикс в формате 10.1.1.0/24:')
#prefix="10.1.1.0/24"
prefix=prefix.split('/')
mask=prefix[1]
network=prefix[0]
mask_bin="1" * int(mask) + "0" * (32-(int(mask)))
mask_ten=[int(mask_bin[0:8],2),int(mask_bin[8:16],2),int(mask_bin[16:24],2),int(mask_bin[24:32],2)]
network=network.split('.')
#print('network=',network,' mask=',mask,' mask_bin=',mask_bin, ' mask_ten=',mask_ten)
print(ip_template.format(int(network[0]),int(network[1]),int(network[2]),int(network[3])))
print(mask_template.format(mask_ten[0],mask_ten[1],mask_ten[2],mask_ten[3],mask))
