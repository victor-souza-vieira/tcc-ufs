def EstacaoAno(hemisferio,dia,mes):

    if hemisferio == 0:
        if mes in (1,2):
            return 'INVERNO'
        elif mes == 3:
            if dia < 21:
                return 'INVERNO'
            else:
                return 'PRIMAVERA'
            
        elif mes in (4,5):
            return 'PRIMAVERA'
        elif mes == 6:
            return 'PRIMAVERA'
            if dia < 21:
                return 'PRIMAVERA'
            else:
                return 'VERAO'
                
        elif mes in (7,8):
            return 'VERAO'
        elif mes == 9:
            if dia < 21:
                return 'VERAO'
            else:
                return 'OUTONO'
                
        elif mes in (10,11):
            return 'OUTONO'
        elif mes == 12:
            if dia < 21:
                return 'OUTONO'
            else:
                return 'INVERNO'
      
    if hemisferio == 1:
        if mes in (1, 2):
            return 'VERAO'
        elif mes == 3:
            if dia < 21:
                return 'VERAO'
            else:
                return 'OUTONO'
        elif mes in (4,5):
            return 'OUTONO'
        elif mes == 6:
            if dia < 21:
                return 'OUTONO'
            else:
                return 'INVERNO'
        elif mes in (7, 8):
            return 'INVERNO'
        elif mes == 9:
            if dia < 21 :
                return 'INVERNO'
            else:
                return 'PRIMAVERA'
        elif mes in (10, 11):
            return 'PRIMAVERA'
        elif mes == 12:
            if dia < 21:
                return 'PRIMAVERA'
            else:
                return 'VERAO'
 
hemisferio = int(input())      
dia = int(input())
mes = int(input())

resultado = EstacaoAno(hemisferio,dia,mes)

print(resultado)
