inputs = input()
nums = inputs.split(' ')
num1 = float(nums[0])
num2 = float(nums[1])
num3 = float(nums[2])
num4 = float(nums[3])

def MediaPond(numA, numB, numC, numD):
    return (numA+(numB*2)+(numC*3)+(numD*4))/10

def AnalisarSituacao(a, b, c, d):
    media = MediaPond(a, b, c, d)
    if media >= 9:
        print('aprovado com louvor')
    elif media >= 7:
        print('aprovado')
    elif media >= 3 and media < 7:
        print('prova final')
    else:
        print('reprovado')
    
AnalisarSituacao(num1, num2 , num3, num4)