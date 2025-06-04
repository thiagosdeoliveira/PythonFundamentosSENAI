# User inserir NOME e IDADE

NOME = input("Digite seu nome")
IDADE = input("Digite sua idade")
print("Seu nome é, ",NOME , "sua idade é ",IDADE)

# Peça dois número e exiba a soma.

print(1+1)
DADO1 = int(input("insira o 1º valor"))
DADO2 = int(input("insira o 2ª valor"))
print("A soma de ", DADO1 ,"+", DADO2 ,"é =", DADO1 + DADO2)

# Peça para o usuário colocar nome, sobrenome, idade, data de nacimento.
# Entrada de Dados
Nome = input("Digite seu nome em MAIUSCULO: ")
Sobrenome = input("Digite seu sobrenome em MAIUSCULO: ")
Idade = int(input("Digite sua idade: "))
Data_de_Nacimento = input("Digite sua data de nascimento considerando a formatação: 00.00.0000")
print("Olá, seu nome completo é: ", Nome, Sobrenome, "tem: ", Idade, "e nasceu em ", Data_de_Nacimento)

#Inserindo o f na frente ele condensa o print em um comando unico entretanto a necessidade de inserir {} para informar a variavel! 

print(f"Paciente {Nome} {Sobrenome }, e sua idade é de: {Idade} e sua data de nascimento {Data_de_Nacimento}")


#Peça dois números ao usuário e exiba o resultado da
# SOMA | SUBTRAÇÃO | MULTIPLICAÇÃO | DIVISÃO


num1 =int(3)
num2 = int(2)

print("O Resultado da soma é ", num1+num2)
print("O Resultado da subtração é ",num1-num2)
print("O Resultado da multiplicação é ",num1*num2)
print("O Resultado da divisão é ", num1/num2)
