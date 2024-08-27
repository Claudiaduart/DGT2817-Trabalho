def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+':
        return adicao(num1, num2)
    elif operacao == '-':
        return subtracao(num1, num2)
    elif operacao == '*':
        return multiplicacao(num1, num2)
    elif operacao == '/':
        return divisao(num1, num2)
    else:
        return "Operação inválida"

saida = 'S'
while saida.upper() != 'N':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado da operação: {resultado}")

        saida = input("Deseja continuar? (S/N): ")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
        break

print("Programa encerrado.")
