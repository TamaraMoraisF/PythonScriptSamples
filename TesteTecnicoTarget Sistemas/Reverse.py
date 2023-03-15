texto = str(input('Digite uma frase pra ver seu reverse: '))
lista = list()

for palavra in texto:
    lista.insert(0, palavra)

for i in range(0, len(texto)):
    print(texto[i], end='')

