hemisferio = int(input())
dia = int(input())
mes = int(input())


def estacoes(h, d, m):
    if h == 0:
        if m == 1 or m == 2 or (m == 12 and d >= 21) or (m == 3 and d <= 20):
            return 'INVERNO'
        elif m == 4 or m == 5 or (m == 3 and d >= 21) or (m == 6 and d <= 20):
            return 'PRIMAVERA'
        elif m == 7 or m == 8 or (m == 6 and d >= 21) or (m == 9 and d <= 20):
            return 'VERAO'
        elif m == 10 or m == 11 or (m == 9 and d >= 21) or (m == 12 and d <= 20):
            return 'OUTONO'
    else:
        if m == 1 or m == 2 or (m == 12 and d >= 21) or (m == 3 and d <= 20):
            return 'VERAO'
        elif m == 4 or m == 5 or (m == 3 and d >= 21) or (m == 6 and d <= 20):
            return 'OUTONO'
        elif m == 7 or m == 8 or (m == 6 and d >= 21) or (m == 9 and d <= 20):
            return 'INVERNO'
        elif m == 10 or m == 11 or (m == 9 and d >= 21) or (m == 12 and d <= 20):
            return 'PRIMAVERA'


estacao = estacoes(hemisferio, dia, mes)
print(estacao)
