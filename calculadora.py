def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x / y

def calculadora():
    print("Calculadora em Python")
    print("------------------------")

    while True:
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha a operação: ")

        if escolha == "5":
            break

        elif escolha in ["1", "2", "3", "4"]:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                resultado = soma(numero1, numero2)
            elif escolha == "2":
                resultado = subtracao(numero1, numero2)
            elif escolha == "3":
                resultado = multiplicacao(numero1, numero2)
            elif escolha == "4":
                resultado = divisao(numero1, numero2)

            print("Resultado:", resultado)

        else:
            print("Erro: escolha inválida!")

calculadora()