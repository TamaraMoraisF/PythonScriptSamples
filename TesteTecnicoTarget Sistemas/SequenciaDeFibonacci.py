numero = int(input('Digite um numero para ver se pertence a sequencia de Fibonacci: '))
segundoNum = 0
primeiroNum = 0
soma = 0
sequenciaFibonacci = [0, 1]


while True:
    if numero in sequenciaFibonacci:
        print('O numero informado pertence a sequencia de Fibonacci!')
        break

    else:
        if numero >= soma:
            if primeiroNum == 0:
                segundoNum = 1
            soma = primeiroNum + segundoNum
            sequenciaFibonacci.append(soma)
            primeiroNum = segundoNum
            segundoNum = soma

        else:
            print('O numero informado não pertence a sequencia de Fibonacci!')
            break

print(sequenciaFibonacci)
