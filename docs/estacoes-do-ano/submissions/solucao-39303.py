hemisferio = int(input())
dia = int(input())
mes = int(input())

def intervF(comp, start, end):
    if comp >= start and comp <= end:
        return True
    else:
        return False

def EstacaoAno(hemsf, dia, mes):
    if hemsf == 1:
        if intervF(mes, 1, 3):
            if mes == 3 and dia > 20:
                print('OUTONO')
            else:
                print('VERAO')
        elif intervF(mes,4,6):
            if mes == 6 and dia > 20:
                print('INVERNO')
            else:
                print('OUTONO')
        elif intervF(mes,7,9):
            if mes == 9 and dia > 20:
                print('PRIMAVERA')
            else:
                print('INVERNO')
        elif intervF(mes,10,12):
            if mes == 12 and dia > 20:
                print('VERAO')
            else:
                print('PRIMAVERA')
    if hemsf == 0:
        if intervF(mes, 1, 3):
            if mes == 3 and dia > 20:
                print('PRIMAVERA')
            else:
                print('INVERNO')
        elif intervF(mes,4,6):
            if mes == 6 and dia > 20:
                print('VERAO')
            else:
                print('PRIMAVERA')
        elif intervF(mes,7,9):
            if mes == 9 and dia > 20:
                print('OUTONO')
            else:
                print('VERAO')
        elif intervF(mes,10,12):
            if mes == 12 and dia > 20:
                print('INVERNO')
            else:
                print('OUTONO')


EstacaoAno(hemisferio, dia, mes)