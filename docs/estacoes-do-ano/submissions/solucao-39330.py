emi = int(input())
dia = int(input())
mes = int(input())

def eRetangulo(e,a,b) :
    if e == 1 :
      if a == 12 and b <= 20 or a == 9 and b >= 21 or a < 12 and a > 9 :
        return 'PRIMAVERA'
      elif a == 12 and b >= 21 or a == 3 and b <= 20 or a == 12 and a < 3 :
        return 'VERAO'
      elif a == 3 and b >= 21 or a == 6 and b <= 20 or a >= 3 and a < 6 :
        return 'OUTONO'
      else :
        return 'INVERNO'
    else :
      if a == 6 and b <= 20 or a == 3 and b >= 21 or a < 6 and a > 3 :
        return 'PRIMAVERA'
      elif a == 6 and b >= 21 or a == 9 and b <= 20 or a >= 6 and a < 9 :
        return 'VERAO'
      elif a == 9 and b >= 21 or a == 12 and b <= 20 or a >= 9 and a < 12 :
        return 'OUTONO'
      else :
        return 'INVERNO'
print(eRetangulo(emi,mes,dia))