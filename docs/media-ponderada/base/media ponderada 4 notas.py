def AnalisarSituacao(n1, n2, n3, n4):
   media = (n1 + 2*n2 + 3*n3 + 4*n4) / 10
   if media >= 9:
      return 'aprovado com louvor'
   elif media >= 7:
      return 'aprovado'
   elif media < 3:
      return 'reprovado'
   else:
      return 'prova final'


valores = input().split()
n1 = float(valores[0])
n2 = float(valores[1])
n3 = float(valores[2])
n4 = float(valores[3])

print(AnalisarSituacao(n1, n2, n3, n4))