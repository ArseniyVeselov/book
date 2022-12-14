# book
fio_list,phone_list = [],[]

def fio(f_i_o):
    return [i for i in f_i_o if i.isalpha()]
     
def phone(p_n):
    return [p_n[i] for i in range(len(p_n)) if p_n[i] in '0123456789']

def del_(ubrat):
    pass
    


f_i_o = input('Введи ФИО -> ').split()
p_n = input('Введи номер -> ')
 
fio_list+=fio(f_i_o)
phone_list+=phone(p_n)

print('ФИО:', *fio_list,end = ' ')
print('Телефон: ',*phone_list,sep='')

ubrat = input('Удалить запись?')
if ubrat.lower() == 'да' or ubrat.lower()== 'yes':
    fio_list.clear()
    phone_list.clear()
    print(fio_list+phone_list, 'дело сделано')
else: print('напиши да')
if input()=='да':
    fio_list.clear()
    phone_list.clear()
    print(fio_list+phone_list, 'дело сделано')
