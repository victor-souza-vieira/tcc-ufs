def estacao_ano(h, d, m):
    dia_do_ano = dia + 30 * (mes - 1)
    if (2*30 + 21) <= dia_do_ano <= (5*30 + 20):
        if h == 1: # Hemisferio Sul
           return 'OUTONO'
        else:  # Hemisferio Norte
           return 'PRIMAVERA' 
    elif (5*30 + 21) <= dia_do_ano <= (8*30 + 20):
        if h == 1:
           return 'INVERNO'
        else:
           return 'VERAO' 
    elif (8*30 + 21) <= dia_do_ano <= (11*30 + 20):
        if h == 1:
           return 'PRIMAVERA'
        else:
           return 'OUTONO'    
    else:
        if h == 1:
           return 'VERAO'
        else:
           return 'INVERNO'  


hemisferio = int(input())
dia = int(input())
mes = int(input())

print(estacao_ano(hemisferio, dia, mes))