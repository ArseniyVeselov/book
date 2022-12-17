name_l , phone_l= ['Пупкин Залупкин Олег'], ['89032787787'] # общие списки

def fio_list(name):                # добавление в список ФИО
     name_l.append(name)

def phone_list(phone):             # добавление в список номеров
     n1=[i for i in phone if i in '0123456789']
     phone_l.append(''.join(n1))

def records():                      # отображение списка
     counter = 0
     for i in range(len(name_l)):
          counter += 1
          print(counter, 'ФИО:', name_l[i], 'Телефон:', phone_l[i])

def removal(number):               # удаление записи
     if number == '1' or number == '2':
          del name_l[int(number) - 1]
          del phone_l[int(number) - 1]
          records()
def amount():                      # количество записей
     print('Количество записей =',len(name_l))

amount()
records()

name = input('Для добвавления введи ФИО: ').title().strip()
phone = input('Введи номер: ').strip()

fio_list(name)
phone_list(phone)
records()

number = input('Удалит запись 1 или 2 ? ')
removal(number)
amount()








