name_l , phone_l= ['Пупкин Залупкин Олег'], ['89032787787'] # общие списки

def fio_list(name):                # добавление в список ФИО
     name_l.append(name)

def phone_list(phone):             # добавление в список номеров
     n1=[i for i in phone if i in '0123456789']
     phone_l.append(''.join(n1))

def zapisi():                      # отображение списка
     counter = 0
     for i in range(len(name_l)):
          counter += 1
          print(counter, 'ФИО:', name_l[i], 'Телефон:', phone_l[i])

def udalenie(nomer):               # удаление записи
     if nomer == '1' or nomer == '2':
          del name_l[int(nomer) - 1]
          del phone_l[int(nomer) - 1]
          zapisi()
def kolichestvo():                 # количество записей
     print('Количество записей =',len(name_l))

kolichestvo()
zapisi()

name = input('Для добвавления введи ФИО: ').title().strip()
phone = input('Введи номер: ').strip()

fio_list(name)
phone_list(phone)
zapisi()

nomer = input('Удалит запись 1 или 2 ? ')
udalenie(nomer)
kolichestvo()









