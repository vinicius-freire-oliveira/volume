def volume():
    # Solicita os valores dos lados do retângulo
    l1 = float(input("Informe o primeiro valor: "))
    l2 = float(input("Informe o segundo valor: "))
    l3 = float(input("Informe o terceiro valor: "))
    
    # Calcula o volume do paralelepípedo
    valor = l1 * l2 * l3

    # Imprime o volume calculado
    print("O volume é de {} m³".format(valor))

# Chama a função para calcular e exibir o volume do paralelepípedo
volume()
