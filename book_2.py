def adding(): # добавление записи
    name_l.append(input('Введи ФИО: ').title().strip())
    phone = input('Введи номер: ').strip()
    n = [i for i in phone if i in '0123456789']
    phone_l.append(''.join(n))
    print('Запись добавлена')
    print()

def removal():  # удаление записи
    records()
    number = input('Введи номер записи для удаления ')
    print('Запись', name_l[int(number) - 1], phone_l[int(number) - 1], 'удалена')
    del name_l[int(number) - 1]
    del phone_l[int(number) - 1]
    print()


def records():  # отображение списка
    counter = 0
    for i in range(len(name_l)):
        counter += 1
        print(counter, 'ФИО:', name_l[i], 'Телефон:', phone_l[i])
    print()
def hat():
    print('Выбери действие:', 'Добавление записи -> 1', 'Удаление записи -> 2', 'Показать список -> 3',
          'Закончить работу программы -> 4', ' ', sep='\n')

def greetings():  # приветствие
    hat()
    action = int(input())
    while action != 4:
        if action == 1:
            adding()
            hat()
        if action == 2:
            removal()
            hat()
        if action == 3:
            records()
            hat()
        action = int(input())


name_l, phone_l = ['Поняев Михаил Сергеевич'], ['89057163112']
greetings()





