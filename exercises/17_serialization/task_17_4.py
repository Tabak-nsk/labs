# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать функцию write_last_log_to_csv.

Аргументы функции:
* source_log - имя файла в формате csv, из которого читаются данные (mail_log.csv)
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Функция write_last_log_to_csv обрабатывает csv файл mail_log.csv.
В файле mail_log.csv находятся логи изменения имени пользователя. При этом, email
пользователь менять не может, только имя.

Функция write_last_log_to_csv должна отбирать из файла mail_log.csv только
самые свежие записи для каждого пользователя и записывать их в другой csv файл.
В файле output первой строкой должны быть заголовки столбцов,
такие же как в файле source_log.

Для части пользователей запись только одна и тогда в итоговый файл надо записать
только ее.
Для некоторых пользователей есть несколько записей с разными именами.
Например пользователь с email c3po@gmail.com несколько раз менял имя:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Из этих трех записей, в итоговый файл должна быть записана только одна - самая свежая:
C-3PO,c3po@gmail.com,16/12/2019 17:24

Для сравнения дат удобно использовать объекты datetime из модуля datetime.
Чтобы упростить работу с датами, создана функция convert_str_to_datetime - она
конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
Полученные объекты datetime можно сравнивать между собой.
Вторая функция convert_datetime_to_str делает обратную операцию - превращает
объект datetime в строку.

Функции convert_str_to_datetime и convert_datetime_to_str использовать не обязательно.

"""

import datetime, csv, re


def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")

def write_last_log_to_csv(source_log,output):
    '''
    Функция write_last_log_to_csv обрабатывает csv файл source_log
    Отбирает самые свежие логи при совпадении поля email
    Записывает в csv файл результат
    '''
    last_log_dict={}
    #открываем csv файл на чтение
    with open(source_log) as f_in:
        reader = csv.reader(f_in)
        #считываем заголовки
        headers = next(reader)
        #print('Headers: ', headers)
        #считываем построчно ф
        for row in reader:
            #print(row)
            login,email,date = row
            #print ('login=',login,' email=',email,' date=',date)
            #Проверяем есть ли запись в словаре с текущим email в ключах
            if last_log_dict.get(email):
                #print('Cовпадение email найдено для email:', email)
                #print ('Данные из файла логов ',[login,date])
                #print ('Данные из финального словаря',last_log_dict.get(email))
                #Если email наден проверяем дату записи
                if convert_str_to_datetime(date)>convert_str_to_datetime(last_log_dict.get(email)[1]):
                    #print('дата свежая нужно обновлять словарь')
                    #если дата свежая обновляем данные словаря
                    last_log_dict.update({email:[login,date]})
            #Если запись в словаре не найдена - добавляем запись с ключом = email
            else:
                last_log_dict.update({email:[login,date]})
        #print(last_log_dict)
        #открываем файл на запись        
        with open(output, 'w') as f_out:
            writer = csv.writer(f_out)
            #записываем заголовок
            writer.writerow(headers)
            for email,value in last_log_dict.items():
                #готовим строку для записи
                to_csv=[value[0],email,value[1]]
                #записываем  строку в csv файл
                writer.writerow(to_csv)
    print('Функция write_last_log_to_csv завершила работу')
    
if __name__ == '__main__':
     write_last_log_to_csv('mail_log.csv','last_log.csv')
    
    
    
    