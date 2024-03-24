from decimal import Decimal, getcontext

# Ajuste a precisão conforme necessário
getcontext().prec = 50

def calculadora():
    var1 = Decimal(input("Digite o primeiro número: "))
    var2 = Decimal(input("Digite o segundo número: "))
    
    # Realiza as operações matemáticas
    soma = var1 + var2
    subtracao = var1 - var2
    multiplicacao = var1 * var2
    
    if var2 != 0:  # Evita divisão por zero
        divisao = var1 / var2
    else:
        divisao = "Erro: Divisão por zero não é permitida."
    
    exponenciacao = var1 ** var2

    # Imprime os resultados
    print(f'Soma: {var1} + {var2} = {soma}')
    print(f'Subtração: {var1} - {var2} = {subtracao}')
    print(f'Multiplicação: {var1} * {var2} = {multiplicacao}')
    print(f'Divisão: {var1} / {var2} = {divisao}')
    print(f'Exponenciação: {var1} ** {var2} = {exponenciacao}')

# Rodando a calculadora
calculadora()
