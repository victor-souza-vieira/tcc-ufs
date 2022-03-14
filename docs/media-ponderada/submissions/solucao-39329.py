numeros = (input())
lista = numeros.split()
def AnalisarSituacao(a,b,c,d):
    media = (a + b*2 + c*3 + d*4) / 10
    if media >= 9:
        print('aprovado com louvor')
    elif media >= 7:
        print('aprovado')
    elif media < 7 and media >= 3:
        print('prova final')
    else:
        print('reprovado')

nota1 = float(lista[0])
nota2 = float(lista[1])
nota3 = float(lista[2])
nota4 = float(lista[3])

AnalisarSituacao(nota1,nota2,nota3,nota4)