def sul(d, m):
    if m >= 9 and mes <= 12:
        if m == 9 and d < 21:
            return 'INVERNO'
        elif m == 12 and d > 20:
            return 'VERAO'
        else:
            return 'PRIMAVERA'
    elif m <= 3:
        if m == 3 and d > 20:
            return 'OUTONO'
        else:
            return 'VERAO'
    elif m <= 6:
        if m == 6 and d > 20:
            return 'INVERNO'
        else:
            return 'OUTONO'
    else:
        return 'INVERNO'

def norte(d, m):
    if m >= 9 and mes <= 12:
        if m == 9 and d < 21:
            return 'VERAO'
        elif m == 12 and d > 20:
            return 'INVERNO'
        else:
            return 'OUTONO'
    elif m <= 3:
        if m == 3 and d > 20:
            return 'PRIMAVERA'
        else:
            return 'INVERNO'
    elif m <= 6:
        if m == 6 and d > 20:
            return 'VERAO'
        else:
            return 'PRIMAVERA'
    else:
        return 'VERAO'
        
hemisferio = int(input())
dia = int(input())
mes = int(input())

if hemisferio == 0:
    print(norte(dia,mes))
else:
    print(sul(dia,mes))