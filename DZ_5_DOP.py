'''
2. ДОП!!!! Задача
Принадлежит ли дата диапазону времени

В программе заданы месяц и год двух дат.
Пользователь вводит еще одну дату (только месяц и год).
Определить, принадлежит ли третья дата диапазону от первой даты до второй включительно.
Задачу решить с использованием структуры данных.
08.1990 - 10.2019
'''
def date_diff(time_1, time_2, time_u):
    time_1 = time_1.split('.')
    time_2 = time_2.split('.')
    time_u = time_u.split('.')

    if not time_1[1] <= time_u[1] <= time_2[1]:
        return False
    elif time_1[1] == time_u[1] and time_1[0] > time_u[0]:
        return False
    elif time_2[1] == time_u[1] and time_2[0] < time_u[0]:
        return False
    return True

time_d = ['08.1990', '10.2019']
print('Диапазон: %s - %s' % (time_d[0], time_d[1]))

time_user = input('Введите дату для проверки: ')

if date_diff(time_d[0], time_d[1], time_user):
    print('Ваша дата принадлежит диапазону от первой даты до второй включительно.')

elif not date_diff(time_d[0], time_d[1], time_user):
    print('Ваша дата Вне заданного диапазона!')



