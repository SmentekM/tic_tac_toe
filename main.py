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
imie = input('Podaj imie: \n')
print(f'Czesc {imie}! \nZagrajmy w kolko i krzyzyk :)\n')
print(""" Zasady gry:
        Zaczynam ja i jestem 'x':)
        Wybierasz numer pola i jestes 'o' :)
        Pola maja nastepujące numery
                1 2 3
                4 5 6
                7 8 9""")


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
    if pole not in '123456789':
        print('Pole zajete. Wybierz ponownie')
        continue
    elif pole == '1' and (pole_1 != '-') or pole == '2' and (pole_2 != '-') or pole == '3' and (pole_3 != '-') \
            or pole == '4' and (pole_4 != '-') or pole == '5' and (pole_5 != '-') or pole == '6' and (pole_6 != '-') \
            or pole == '7' and (pole_7 != '-') or pole == '8' and (pole_8 != '-') or pole == '9' and (pole_9 != '-'):
        print('Pole zajete. Wybierz ponownie')
        continue

    if pole == '1':

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

        elif pole == '4':
            pole_4 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '6':
            pole_6 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '7':
            pole_7 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '9':
            pole_9 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '8':
            pole_8 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_7 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            pole = input('Podaj numer pola: ')
            if pole == '4':
                pole_4 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '6':
                pole_6 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '9':
                pole_9 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '3':
                pole_3 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_6 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                pole = input('Podaj numer pola: ')

                if pole == '9':
                    pole_9 = gracz
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                    print('Ruch wykonuje komputer')
                    pole_4 = komputer
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                elif pole == '4':
                    pole_4 = gracz
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                    print('Ruch wykonuje komputer')
                    pole_9 = komputer
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    elif pole == '2':

        pole_2 = gracz
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_6 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        pole = input('Podaj numer pola: ')
        if pole == '1':
            pole_1 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '3':
            pole_3 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '7':
            pole_7 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '8':
            pole_8 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '9':
            pole_9 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '4':
            pole_4 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_3 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            pole = input('Podaj numer pola: ')
            if pole == '1':
                pole_1 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_7 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '8':
                pole_8 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_7 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '9':
                pole_9 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_7 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '7':
                pole_7 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_9 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    elif pole == '3':

        pole_3 = gracz
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_2 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        pole = input('Podaj numer pola: ')
        if pole == '1':
            pole_1 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '4':
            pole_4 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '6':
            pole_6 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '7':
            pole_7 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '9':
            pole_9 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '8':
            pole_8 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_9 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            pole = input('Podaj numer pola: ')
            if pole == '4':
                pole_4 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_1 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '6':
                pole_6 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_1 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '7':
                pole_7 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_1 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '1':
                pole_1 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_6 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                pole = input('Podaj numer pola: ')

                if pole == '7':
                    pole_7 = gracz
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                    print('Ruch wykonuje komputer')
                    pole_4 = komputer
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                elif pole == '4':
                    pole_4 = gracz
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                    print('Ruch wykonuje komputer')
                    pole_7 = komputer
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    elif pole == '4':

        pole_4 = gracz
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_2 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        pole = input('Podaj numer pola: ')
        if pole == '1':
            pole_1 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '3':
            pole_3 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '6':
            pole_6 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '7':
            pole_7 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '9':
            pole_9 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '8':
            pole_8 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_3 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            pole = input('Podaj numer pola: ')
            if pole == '1':
                pole_1 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_7 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '6':
                pole_6 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_7 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '9':
                pole_9 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_1 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '7':
                pole_7 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_1 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    elif pole == '6':

        pole_6 = gracz
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_2 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        pole = input('Podaj numer pola: ')
        if pole == '1':
            pole_1 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '3':
            pole_3 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '4':
            pole_4 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '7':
            pole_7 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '9':
            pole_9 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '8':
            pole_8 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_1 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            pole = input('Podaj numer pola: ')
            if pole == '3':
                pole_3 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_9 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '4':
                pole_4 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '7':
                pole_7 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '9':
                pole_9 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    elif pole == '7':

        pole_7 = gracz
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_2 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        pole = input('Podaj numer pola: ')
        if pole == '1':
            pole_1 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '4':
            pole_4 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '6':
            pole_6 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '3':
            pole_3 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '9':
            pole_9 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '8':
            pole_8 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_9 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            pole = input('Podaj numer pola: ')
            if pole == '4':
                pole_4 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_1 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '6':
                pole_6 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_1 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '3':
                pole_3 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_1 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '1':
                pole_1 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_4 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                pole = input('Podaj numer pola: ')

                if pole == '3':
                    pole_3 = gracz
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                    print('Ruch wykonuje komputer')
                    pole_6 = komputer
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                elif pole == '6':
                    pole_6 = gracz
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                    print('Ruch wykonuje komputer')
                    pole_3 = komputer
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    elif pole == '8':

        pole_8 = gracz
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_6 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        pole = input('Podaj numer pola: ')
        if pole == '1':
            pole_1 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '2':
            pole_2 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '7':
            pole_7 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '9':
            pole_9 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '3':
            pole_3 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_4 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '4':
            pole_4 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_3 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            pole = input('Podaj numer pola: ')
            if pole == '1':
                pole_1 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_7 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '2':
                pole_2 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_7 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '9':
                pole_9 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_7 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '7':
                pole_7 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_9 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    elif pole == '9':

        pole_9 = gracz
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        print('Ruch wykonuje komputer')
        pole_2 = komputer
        print(
            f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
        pole = input('Podaj numer pola: ')
        if pole == '1':
            pole_1 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '4':
            pole_4 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '6':
            pole_6 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '3':
            pole_3 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '7':
            pole_7 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_8 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

        elif pole == '8':
            pole_8 = gracz
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            print('Ruch wykonuje komputer')
            pole_7 = komputer
            print(
                f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
            pole = input('Podaj numer pola: ')
            if pole == '1':
                pole_1 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '4':
                pole_4 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '6':
                pole_6 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_3 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

            elif pole == '3':
                pole_3 = gracz
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                print('Ruch wykonuje komputer')
                pole_6 = komputer
                print(
                    f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                pole = input('Podaj numer pola: ')

                if pole == '1':
                    pole_1 = gracz
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                    print('Ruch wykonuje komputer')
                    pole_4 = komputer
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                elif pole == '4':
                    pole_4 = gracz
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')
                    print('Ruch wykonuje komputer')
                    pole_1 = komputer
                    print(
                        f'{pole_1} | {pole_2} | {pole_3}\n---------\n{pole_4} | {pole_5} | {pole_6}\n---------\n{pole_7} | {pole_8} | {pole_9}\n')

    if pole_1 == pole_2 == pole_3 == komputer or pole_4 == pole_5 == pole_6 == komputer or\
        pole_7 == pole_8 == pole_9 == komputer or pole_1 == pole_4 == pole_7 == komputer or\
        pole_2 == pole_5 == pole_8 == komputer or pole_3 == pole_6 == pole_9 == komputer or \
        pole_1 == pole_5 == pole_9 == komputer or pole_3 == pole_5 == pole_7 == komputer:
        print('Przegrana!')
        break
    # brak warunku wygrania przeciwnika - niemozliwe
    else:
        print('Remis!')
        break
