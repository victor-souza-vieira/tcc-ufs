hem = float(input())
a = float(input())
b = float(input())
data = (a, b)
if hem == 1:
    if b in (1,2):
        print('VERAO')
    elif b == 3:
        if a < 21:
          print('VERAO')
        else:
          print('OUTONO')
    elif b in (4, 5):
           print('OUTONO')
    elif b == 6:
        if a < 21:
           print('OUTONO')
        else:
            print('INVERNO')
    elif b in (7, 8):
        print('INVERNO')
    elif b == 9:
        if a < 21:
            print('INVERNO')
        else:
            print('PRIMAVERA')
    elif b in (10, 11):
        print('PRIMAVERA')
    elif b == 12:
        if a < 21:
            print('PRIMAVERA')
        else:
            print('VERAO')
elif hem == 0:
    if b in (1,2):
        print('INVERNO')
    elif b == 3:
        if a < 21:
          print('INVERNO')
        else:
          print('PRIMAVERA')
    elif b in (4, 5):
           print('PRIMAVERA')
    elif b == 6:
        if a < 21:
           print('PRIMAVERA')
        else:
            print('VERAO')
    elif b in (7, 8):
        print('VERAO')
    elif b == 9:
        if a < 21:
            print('VERAO')
        else:
            print('OUTONO')
    elif b in (10, 11):
        print('OUTONO')
    elif b == 12:
        if a < 21:
            print('OUTONO')
        else:
            print('INVERNO')