import random

# Computador seleciona um número aleatório entre 1 e 300
numero_secreto = random.randint(1, 300)

def busca_binaria(inicio, fim):
    tentativas = 0
    while inicio <= fim:
        # Escolhe o ponto médio
        palpite = (inicio + fim) // 2
        tentativas += 1
        if palpite < numero_secreto:
            inicio = palpite + 1
        elif palpite > numero_secreto:
            fim = palpite - 1
        else:
            return palpite, tentativas

# Testa o algoritmo de busca binária para encontrar o número
resultado, tentativas = busca_binaria(1, 300)
print(f"O número selecionado foi {resultado} e foi encontrado em {tentativas} tentativas.")
