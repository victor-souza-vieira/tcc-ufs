nota = input()
spli = nota.split(' ')
no1 = spli[0]
no2 = spli[1]
no3 = spli[2]
no4 = spli[3]
no1, no2, no3, no4 = float(no1), float(no2), float(no3), float(no4)

def AnalisarSituacao(n1, n2, n3, n4) :
    media = (1*n1 + 2*n2 + 3*n3 + 4*n4)/(1+2+3+4)

    if media >= 9 :
        return 'aprovado com louvor'
    elif media >= 7 :
        return 'aprovado'
    elif media >= 3 and media < 7 :
        return 'prova final'
    else : 
        return 'reprovado'

print(AnalisarSituacao(no1,no2,no3,no4))