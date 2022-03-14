# 0
# ver�o: de 21 de junho a 20 de setembro; 6,7,8,9
# outono: de 21 de setembro a 20 de dezembro;9,10,11,12
# inverno: de 21 de dezembro a 20 de mar�o;12,1,2,3
# primavera: de 21 de mar�o a 20 de junho. 3,4,5,6


# Esta��es do ano no hemisf�rio sul 1:
# ver�o: de 21 de dezembro a 20 de mar�o;  12,1,2,3
# outono: de 21 de mar�o a 20 de junho; 3,4,5,6
# inverno: de 21 de junho a 20 de setembro;6,7,8,9
# primavera: de 21 de setembro a 20 de dezembro. 9,10,11,12

hemis = int(input())
dia = int(input())
mes = int(input())

def EstacaoAno(hemis,dia,mes):
    if hemis == 0:
        if mes == 12:
            if dia <= 20:
                print('OUTONO')
            else:
                print('INVERNO')

        elif mes == 9:
            if dia <= 20:
                print('VERAO')
            else:
                print('OUTONO')

        elif mes == 3:
            if dia <= 20:
                print('INVERNO')
            else:
                print('PRIMAVERA')

        elif mes == 6:
            if dia <= 20:
                print('PRIMAVERA')
            else:
                print('VERAO')

        elif mes == 10 or mes == 11:
            print('OUTONO')


        elif mes == 1 or mes == 2:
            print('INVERNO')

        elif mes == 4 or mes == 5:
            print('PRIMAVERA')


        elif mes == 7 or mes == 8:
            print('VERAO')
    elif hemis == 1:
        if mes == 12:
            if dia <= 20:
                print('PRIMAVERA')
            else:
                print('VERAO')

        elif mes == 9:
            if dia <= 20:
                print('INVERNO')
            else:
                print('PRIMAVERA')

        elif mes == 3:
            if dia <= 20:
                print('VERAO')
            else:
                print('OUTONO')

        elif mes == 6:
            if dia <= 20:
                print('OUTONO')
            else:
                print('INVERNO')

        elif mes == 10 or mes == 11:
            print('PRIMAVERA')


        elif mes == 1 or mes == 2:
            print('VERAO')

        elif mes == 4 or mes == 5:
            print('OUTONO')


        elif mes == 7 or mes == 8:
            print('INVERNO')

EstacaoAno(hemis,dia,mes)
