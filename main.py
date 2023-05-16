pole_1 = '-'
pole_2 = '-'
pole_3 = '-'
pole_4 = '-'
pole_5 = '-'
pole_6 = '-'
pole_7 = '-'
pole_8 = '-'
pole_9 = '-'
komputer = 'x'
gracz = 'o'


print(f'{pole_1} | {pole_2} | {pole_3}\n'
      f'---------\n'
      f'{pole_4} | {pole_5} | {pole_6}\n'
      f'---------\n'
      f'{pole_7} | {pole_8} | {pole_9}\n')
print('Komputer wykonuje ruch :)')
pole_5 = komputer
print(f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
while True:
    pole = input('Podaj numer pola: ')

    if pole == '1':
#komentarz
        pole_1 = gracz
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_2 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        pole = input('Podaj numer pola: ')
        if pole == '3':
            pole_3 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_8 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    elif pole == '9':
        pole_9 = gracz
        print(f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | '
              f'{pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
    if pole_1 == pole_2 == pole_3 == komputer or pole_4 == pole_5 == pole_6 == komputer or\
        pole_7 == pole_8 == pole_9 == komputer or pole_1 == pole_4 == pole_7 == komputer or\
        pole_2 == pole_5 == pole_8 == komputer or pole_3 == pole_6 == pole_9 == komputer or \
        pole_1 == pole_5 == pole_9 == komputer or pole_3 == pole_5 == pole_7 == komputer:
        print('Wybrywa komputer!')
        break
# elif pole_1 == pole_2 == pole_3 == gracz or pole_4 == pole_5 == pole_6 == gracz or\
#     pole_7 == pole_8 == pole_9 == gracz or pole_1 == pole_4 == pole_7 == gracz or\
#     pole_2 == pole_5 == pole_8 == gracz or pole_3 == pole_6 == pole_9 == gracz or \
#     pole_1 == pole_5 == pole_9 == gracz or pole_3 == pole_5 == pole_7 == gracz:
#     print('Wygrywa gracz!')
# else:
#     print('Remis')
