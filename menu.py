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

def shell_sort(v):
    n = len(v)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = v[i]
            j = i
            while j >= gap and v[j - gap] > temp:
                v[j] = v[j - gap]
                j -= gap
            v[j] = temp
        gap //= 2
    return v

def merge_sort(v):
    if len(v) > 1:
        mid = len(v) // 2
        L = v[:mid]
        R = v[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                v[k] = L[i]
                i += 1
            else:
                v[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            v[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            v[k] = R[j]
            j += 1
            k += 1
    return v

def quick_sort(v):
    if len(v) <= 1:
        return v
    pivot = v[len(v) // 2]
    left = [x for x in v if x < pivot]
    middle = [x for x in v if x == pivot]
    right = [x for x in v if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main():
    vetor = None
    while True:
        print("\n MENU DE ORDENAÇÃO ")
        print("1. Gerar vetor aleatório")
        print("2. Inserir vetor manualmente")
        print("3. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            while True:
                try:
                    tamanho = int(input("Digite o tamanho do vetor que deseja gerar: "))
                    if tamanho <= 0:
                        print("Erro: O tamanho do vetor deve ser maior que 0.")
                        continue
                    vetor = gerar_vetor(tamanho)
                    break
                except ValueError:
                    print("Erro: Digite um número inteiro válido.")

        elif escolha == '2':
            while True:
                try:
                    entrada = input(
                        "Digite os números separados por espaços (use ',' ou '.' para decimais): "
                    ).strip()
                    entrada = entrada.replace(',', '.')
                    vetor = [float(valor) for valor in entrada.split()]
                    if not vetor:
                        print("Erro: O vetor não pode estar vazio.")
                        continue
                    print("Vetor inserido:", vetor)
                    break
                except ValueError:
                    print("Erro: Certifique-se de digitar apenas números válidos, separados por espaços.")

        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

        while vetor:
            print("\nVetor gerado/desordenado:", vetor)
            print("\nEscolha o algoritmo de ordenação:")
            print("1. Bubble Sort")
            print("2. Shell Sort")
            print("3. Merge Sort")
            print("4. Quick Sort")
            print("5. Inserir novo vetor")
            print("6. Sair")

            opcao = input("Digite o número da opção desejada: ").strip()

            if opcao == '1':
                resultado = bubble_sort(vetor.copy())
                print("Vetor ordenado com Bubble Sort:", resultado)
            elif opcao == '2':
                resultado = shell_sort(vetor.copy())
                print("Vetor ordenado com Shell Sort:", resultado)
            elif opcao == '3':
                resultado = merge_sort(vetor.copy())
                print("Vetor ordenado com Merge Sort:", resultado)
            elif opcao == '4':
                resultado = quick_sort(vetor.copy())
                print("Vetor ordenado com Quick Sort:", resultado)
            elif opcao == '5':
                vetor = None
                break
            elif opcao == '6':
                print("Saindo...")
                return
            else:
                print("Opção inválida. Tente novamente.")

            if vetor:
                while True:
                    repetir = input("\nDeseja utilizar o mesmo vetor para outra ordenação? (s/n): ").strip().lower()
                    if repetir == 's':
                        break
                    elif repetir == 'n':
                        vetor = None
                        break
                    else:
                        print("Erro: Digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()
