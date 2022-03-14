def AnalisarSituacao(media):
    if media >= 9 :
      return('aprovado com louvor')
    if media >= 7 :
      return('aprovado')
    if media < 3 :
      return('reprovado')
    elif media >= 3 and media <7 :
      return('prova final')
       
n = input()
x = n.split(' ')
a = float(x[0])
b = float(x[1])
c = float(x[2])
d = float(x[3])
media = (a*1 + b*2 + c*3 + d*4)/10
      
print(AnalisarSituacao(media))
