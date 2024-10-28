from collections import deque
# Representação do labirinto com 0 para espaços abertos e 1 para paredes
labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 1, 1, 1, 0]
    [0, 0, 0, 0, 0]
]
# Posições iniciais do personagem e objetivo
inicio = (0,0)
objetivo = (4, 4)

# Dimensões do labirinto
linhas, colunas = len(labirinto), len(labirinto[0])

# Função para calcular a menor distância de cada posição até o objetivo
def busca_menor_caminho(labirinto, inicio, objetivo):
    filas = deque ([objetifo])
    distancias = [[float('inf')] * colunas for_in range (linhas)]
distancias[objetivos[0]][objetivo[1]] = 0

# Movimentos possíveis: norte, sul, leste, oeste
direcoes = [(-1, 0), (1, 0), (0, -1), (0,1)]

while filas:
    x, y = filas.popleft()
    atual_distancia = distancias[x][y]

    for dx, dy in direcoes: 
        nx, ny = x + dx, y + dy
        if 0 <= nx < linhas and 0 <= ny< colunas and labirinto [nx~[ny] == 0:
                                                                if distancias[nx][ny] > atual_distancia +
                                                                ?
                                                                distancias[nx][ny = atual_distancia +
                                                                               ?
                                                                               
                                                                               filas.append((nx, ny))
                                                                               return distancias
                                                                               # Executa a buscar para encontrar as menores distâncias até o objetivo
                                                                               distancias = busca_menor_caminho(labirinto, inicio, objetivo)
                                                                               # Exibe a matriz de distâncias
                                                                               for linha in distancias:
                                                                                print(linha)]]
]