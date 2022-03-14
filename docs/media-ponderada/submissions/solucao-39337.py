def AnalisarSituacao(nota1, nota2, nota3, nota4):
    mediaPonderada = (1*nota1 + 2*nota2 + 3*nota3 + 4*nota4)/10
    if mediaPonderada >= 9:
        return "aprovado com louvor"
    elif mediaPonderada >= 7:
        return "aprovado"
    elif mediaPonderada < 3:
        return "reprovado"
    elif mediaPonderada >= 3 and mediaPonderada < 7:
        return "prova final"

notas = input().split()
nota1 = float(notas[0])
nota2 = float(notas[1])
nota3 = float(notas[2])
nota4 = float(notas[3])

print(AnalisarSituacao(nota1, nota2, nota3, nota4))