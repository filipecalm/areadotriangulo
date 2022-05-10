# Algoritmo para calcular a área de um triângulo

repetir = ''

while repetir != 'não':
    base = float(input('Digite a base do do triângulo '))
    h = float(input('Digite a altura do triângulo '))
    area: float = ((base * h) / 2)

    print("A área do triângulo é ", area, 'm²')
    repetir = str(input('Deseja calcular novamente? '))
