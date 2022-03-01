import subprocess as sp


def solucao(entrada):
    pilha = []
    count_diamonds = 0
    for item in entrada:
        if item == '.':
            continue
        if item == '<':
            pilha.append(item)
            continue
        if item == '>' and len(pilha) > 0:
            pilha.pop()
            count_diamonds = count_diamonds + 1
        elif item == 'a':
            pilha.pop()
        elif item == 'b':
            pilha.pop()
        elif item == 'a':
            pilha.pop()
        elif item == 'b':
            pilha.pop()
        elif item == 'a':
            pilha.pop()
        elif item == 'b':
            pilha.pop()
        elif item == 'a':
            pilha.pop()
        elif item == 'b':
            pilha.pop()
    return count_diamonds


def main2():
    while True:
        n = int(input())
        if n == 0: break

        cartas = [i for i in range(1, n + 1)]
        descarte = []

        while len(cartas) >= 2:
            descarte.append(cartas.pop(0))
            cartas.append(cartas.pop(0))

        saida = 'Discarded cards: '
        for carta in descarte:
            saida = saida + str(carta) + ', '
        saida = saida[:-2] + '\nRemaining card: ' + str(cartas.pop())
        print(saida)


def main():
    n = int(input())
    for _ in range(n):
        entrada = list(input())
        print(solucao(entrada))


def mainx():
    n = int(input())
    for _ in range(n):
        entrada = list(input())
        print(solucao(entrada))


def sample():
    b = sp.getoutput('python3 -m radon raw example.py -j')
    print(b.lstrip())


if __name__ == '__main__':
    sample()
