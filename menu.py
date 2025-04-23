import random

def gerar_vetor(tamanho, minimo=1, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]

def bubble_sort(v):
    n = len(v)
    for i in range(n):
        for j in range(0, n - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
    return v

def main():
    while True:
        try:
            print("\n MENU DE ORDENAÇÃO ")
            tamanho = int(input("Digite o tamanho do vetor que deseja gerar (ou 0 para sair): "))
            if tamanho <= 0:
                print("Saindo...")
                break

            vetor = gerar_vetor(tamanho)
            print("Vetor gerado:", vetor)
        except ValueError:
            print("Erro: Digite um número válido.")
            continue

        print("\nEscolha o algoritmo de ordenação:")
        print("1. Bubble Sort")
        print("2. Selection Sort (a implementar)")
        print("3. Insertion Sort (a implementar)")
        print("4. Merge Sort (a implementar)")
        print("5. Quick Sort (a implementar)")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            resultado = bubble_sort(vetor.copy())
            print("Vetor ordenado com Bubble Sort:", resultado)
        elif escolha == '2':
            print("Selection Sort ainda não implementado.")
        elif escolha == '3':
            print("Insertion Sort ainda não implementado.")
        elif escolha == '4':
            print("Merge Sort ainda não implementado.")
        elif escolha == '5':
            print("Quick Sort ainda não implementado.")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
