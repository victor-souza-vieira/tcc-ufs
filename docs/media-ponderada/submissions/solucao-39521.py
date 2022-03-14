

(n1,n2,n3,n4) = input().split()

A = float(n1)
B = float(n2)
C = float(n3)
D = float(n4)

mediaPonderada = (A + (B * 2) + (C*3) + (D*4))/10

def AnalisarSituacao(media):
    if media >= 9:
        print('aprovado com louvor')
    elif media >= 7:
        print('aprovado')
    elif (media >=3) and (media <7):
        print ('prova final')
    else:
        print('reprovado')

AnalisarSituacao(mediaPonderada)


