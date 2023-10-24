# Função para somar o valor da memória com um número
def somar(memoria, numero):
    return memoria + numero

# Função para subtrair o valor da memória por um número
def subtrair(memoria, numero):
    return memoria - numero

# Função para multiplicar o valor da memória por um número
def multiplicar(memoria, numero):
    return memoria * numero

# Função para dividir o valor da memória por um número
def dividir(memoria, numero):
    if numero == 0:
        print("Não é possível dividir por zero.")
        return memoria
    return memoria / numero

# Função para limpar o valor da memória (zerar)
def limpar_memoria():
    return 0

# Estado inicial da memória
memoria = 0

while True:
    print("Estado da memória:", memoria)
    print("Opções:")
    print("(1) Somar")
    print("(2) Subtrair")
    print("(3) Multiplicar")
    print("(4) Dividir")
    print("(5) Limpar memória")
    print("(6) Sair do programa")
    
    opcao = input("Qual opção você deseja? ")

    if opcao == "1":
        numero = float(input("Informe um número para somar: "))
        memoria = somar(memoria, numero)
    elif opcao == "2":
        numero = float(input("Informe um número para subtrair: "))
        memoria = subtrair(memoria, numero)
    elif opcao == "3":
        numero = float(input("Informe um número para multiplicar: "))
        memoria = multiplicar(memoria, numero)
    elif opcao == "4":
        numero = float(input("Informe um número para dividir: "))
        memoria = dividir(memoria, numero)
    elif opcao == "5":
        memoria = limpar_memoria()
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

print("Programa encerrado.")
