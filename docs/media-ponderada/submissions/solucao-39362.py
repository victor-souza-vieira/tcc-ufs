def AnalisarSituacao(n1, n2, n3, n4):
    mediaP = (n1 + n2*2 + n3*3 + n4*4) / 10
    if mediaP >= 9:
        return 'aprovado com louvor'
    elif mediaP >= 7:
        return 'aprovado'
    elif mediaP < 3: 
        return 'reprovado'
    else:
        return 'prova final'
        
a1, a2, a3, a4 = input().split()
a1 = float(a1)
a2 = float(a2)
a3 = float(a3)
a4 = float(a4)
sit = AnalisarSituacao(a1, a2, a3, a4)
print(sit)