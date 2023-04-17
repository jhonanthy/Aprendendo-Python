#calculadora simples em Python como exercicio de programação.
# Feito por Jhonanthy Almeida.

operacao = input("Digite a operação eu deseja executar (+, -, *, /): ")
num1     = int(input("Digite um numero inteiro para a operação: ")) #utilizei numeros inteiros mesmo mas poderia ser float etc...
num2     = int(input("Digite um segundo e ultimo numero inteiro para a operação:    "))
def RealizaCalculo(num1,num2,operacao):
    if operacao == '+':
        return  num1 + num2         
    elif operacao == '-':
        return  num1 - num2
    elif operacao == '*':
        return  num1 * num2
    elif operacao == '/':
        return  num1 / num2
    else:
        print("Não foi selecionada nenhuma operação!")
    
resultadoCalculo = RealizaCalculo(num1,num2,operacao)

#Printando resultado do calculo.    
#if len(resultadoCalculo)== 0:
print("O resultado eh: ", resultadoCalculo)