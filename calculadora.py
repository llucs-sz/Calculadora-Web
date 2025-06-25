def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def calculadora():
    print("Calculadora Digital Simples")
    while True:
        print("\nEscolha a operação:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        escolha = input("Digite a opção (0-4): ")

        if escolha == "0":
            print("Saindo da calculadora. Até logo!")
            break

        if escolha not in ["1", "2", "3", "4"]:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite números.")
            continue

        if escolha == "1":
            resultado = somar(num1, num2)
        elif escolha == "2":
            resultado = subtrair(num1, num2)
        elif escolha == "3":
            resultado = multiplicar(num1, num2)
        elif escolha == "4":
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()
