n1, n2, n3, n4 = input().split()
n1 = float (n1)
n2 = float (n2)
n3 = float (n3)
n4 = float (n4)

media = (n1*1+n2*2+n3*3+n4*4)/10

def AnalisarSituacao (media):
    if media>=9:
        return 'aprovado com louvor'
    elif media>=7:
        return 'aprovado'
    elif media<3:
        return 'reprovado'
    else:
        return 'prova final'
        
x = AnalisarSituacao(media)
print (x)
