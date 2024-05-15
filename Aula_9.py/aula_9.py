lista = [1,6,6,9]
numero = int(input('>>'))
lista.append(numero)
c = 4
soma = 0
while c > 0:
    for n in lista:
        if n % 2 == 0:
           soma = soma + n
           print(soma)

