def adding():
    def fio_list():                # добавление в список ФИО
        name_l.append(input('Введи ФИО: ').title().strip())
    fio_list()

    def phone_list():             # добавление в список номеров
        phone = input('Введи номер: ').strip()
        n=[i for i in phone if i in '0123456789']
        phone_l.append(''.join(n))
    phone_list()

def removal():               # удаление записи
    records()
    number = input('Введи номер записи для удаления ')
    #if number == '1' or number == '2':
    print('Запись',name_l[int(number)-1],phone_l[int(number)-1], 'удалена')
    del name_l[int(number) - 1]
    del phone_l[int(number) - 1]
    #records()  
    
def records():                      # отображение списка
     counter = 0
     for i in range(len(name_l)):
          counter += 1
          print(counter, 'ФИО:', name_l[i], 'Телефон:', phone_l[i])
    
def greetings(): # приветствие
    print('Выбери действие:','Добавление записи -> 1','Удаление записи -> 2', 'Показать список -> 3', 'Закончить работу программы -> 4',sep='\n')
    action = input()
    while action!= '4':
        if action == '1':
            adding()
            greetings()
        elif action == '2':
            removal()
            greetings()
        elif action == '3':
            records()
            greetings()
        elif action == '4':
            exit()
               
name_l, phone_l = ['Поняев Михаил Сергеевич'],['89057163112']
greetings()





