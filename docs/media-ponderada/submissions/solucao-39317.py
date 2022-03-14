notas = input()
eachNota = notas.split()
n1 = float(eachNota [0])
n2 = float(eachNota [1])
n3 = float(eachNota [2])
n4 = float(eachNota [3])

def AnalisarSituacao(N1,N2,N3,N4):
    media = (1*N1 + 2*N2 + 3*N3 + 4*N4)/10
    if media >= 9:
        return 'aprovado com louvor'
    elif media >= 7:
        return 'aprovado'
    elif media < 3:
        return 'reprovado'
    else:
        return 'prova final'
situacao = AnalisarSituacao(n1,n2,n3,n4)
print(situacao)