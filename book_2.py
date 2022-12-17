def adding():
    def fio_list(name):                # добавление в список ФИО
         name_l.append(name)

    def phone_list(phone):             # добавление в список номеров
         n=[i for i in phone if i in '0123456789']
         phone_l.append(''.join(n))

def removal():               # удаление записи
    #
    number = input('Введи номер записи для удаления')
    if number == '1' or number == '2':
        del name_l[int(number) - 1]
        del phone_l[int(number) - 1]
    #    


def greetings():
    print('Выбери действие:','Добавление записи -> 1','Удаление записи -> 2', 'Показать список -> 3', 'Закончить работу программы -> 4',sep='\n')
    action = input()
    if action == '1':
        adding()
    elif action == '2':
        removal

name_l, phone_l = [],[]
        
        
greetings()
adding()
    

name = input('Введи ФИО: ').title().strip()
phone = input('Введи номер: ').strip()








