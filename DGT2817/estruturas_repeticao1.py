# Crie uma variável chamada entrada_idade e atribua a ela o valor ''
entrada_idade = ''

# Instrução while para verificar se o valor atribuído à variável entrada_idade é diferente de 0
while entrada_idade != '0':
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    if entrada_idade:
        print(f'Número digitado: {entrada_idade}')

print("Programa encerrado. Obrigado por participar!")