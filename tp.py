import numpy as np
import matplotlib.pyplot as plt
from igraph import *

# Cria a matriz de adjacência do tabuleiro 8x8
def geraTabuleiro():

    # Cria uma matriz de adjacência para representar o grafo
    chess_board = np.zeros((64,64))

    # Nesta parte são adicionadas as arestas do grafo.
    for j in range(64):
        for i in range(1,8):
            if (((j-9*i) >= 0) and (j-9*i < 64) and ((j-9*i)//8 == ((j//8)-i))):
                chess_board[j, j-9*i] = 1
            if (((j-8*i) >= 0) and (j-8*i < 64)):
                chess_board[j, j-8*i] = 1
            if (((j-7*i) >= 0) and (j-7*i < 64) and ((j-7*i)//8 == ((j//8)-i))):
                chess_board[j, j-7*i] = 1
            if (((j-1*i) >= 0) and (j-1*i < 64) and ((j-1*i)//8 == (j//8))):
                chess_board[j, j-1*i] = 1
            if (((j+1*i) >= 0) and (j+1*i < 64) and ((j+1*i)//8 == (j//8))):
                chess_board[j, j+1*i] = 1
            if (((j+7*i) < 64) and ((j+7*i) >= 0) and ((((j+7*i)//8)-i) == (j//8))):
                chess_board[j, j+7*i] = 1
            if (((j+8*i) < 64) and (j+8*i) >= 0):
                chess_board[j, j+8*i] = 1
            if (((j+9*i) < 64) and ((j+9*i) >= 0) and ((((j+9*i)//8)-i) == (j//8))):
                chess_board[j, j+9*i] = 1

    return chess_board

# Algoritmo Bron-Kerbosch
def bronKerbosch(R, P, X):
    global V, Clq
    if len(P) == 0 and len(X) == 0:
        Clq.append(R)
        return

    for v in P[:]:
        t1 = R + [v]
        t2 = list(set(P) & set(g.neighbors(v)))
        t3 = list(set(X) & set(g.neighbors(v)))

        bronKerbosch(t1, t2, t3)
        P.remove(v)
        X.append(v)

def visualizaGrafo():
    chess_board = geraTabuleiro()
    g = Graph.Adjacency(chess_board.tolist(), ADJ_UNDIRECTED)
    layout = g.layout_grid()

    g = g.complementer(False)
    V = list(range(64))
    adj = g.get_adjacency()

    bronKerbosch([], V, [])

    r8 = [i for i in Clq if len(i) == 8]
    print(len(r8))

    #for k in range(len(r8)):
    #    cmap = []
    #    for i in range(64):
    #        if i in r8[k]: cmap.append("blue")
    #        else: cmap.append("white")

    #    plot(g, layout=layout, vertex_color=cmap)
    #    s = input()
    #    if s == 'q': exit()

def visualizaMatriz():
    chess_board = geraTabuleiro()
    print(chess_board)

def main():
    print("--------------------------")
    print("-        8 Rainhas       -")
    print("-  Por: Arthur G., 2019  -")
    print("--------------------------")
    key = 0

    while (key != 3):
        print("\n1 - Visualizar as soluções pelo grafo")
        print("2 - Visualizar a matriz de adjacência")
        print("3 - Sair\n")

        key = int(input(''))
        if (key == 1):
            visualizaGrafo()
        if (key == 2):
            visualizaMatriz()

    print("Programa Encerrado!")

if __name__ == '__main__':
    main()
