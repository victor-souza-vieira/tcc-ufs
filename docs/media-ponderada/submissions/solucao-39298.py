a1, a2, a3, a4 = input().split()
a1 = float(a1)
a2 = float(a2)
a3 = float(a3)
a4 = float(a4)
media = ((a1*1) + (a2*2) + (a3*3) + (a4*4)) / 10
if media >= 9:
    print('aprovado com louvor')
elif media >= 7:
    print('aprovado')
elif 3 <= media < 7 :
    print('prova final')
elif media < 3:
    print('reprovado')