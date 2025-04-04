from collections import defaultdict

class Grafo:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.ordem = 0
        self.tamanho = 0

    def adiciona_vertice(self, u):
        if u not in self.adj_list:
            self.adj_list[u] = []
            self.ordem += 1

    def adiciona_aresta(self, u, v, peso):
        if peso < 0:
            print("Pesos negativos não são permitidos.")
            return

        if u not in self.adj_list:
            self.adiciona_vertice(u)
        if v not in self.adj_list:
            self.adiciona_vertice(v)

        for i, (vizinho, _) in enumerate(self.adj_list[u]):
            if vizinho == v:
                self.adj_list[u][i] = (v, peso)
                return

        self.adj_list[u].append((v, peso))
        self.tamanho += 1

    def remove_aresta(self, u, v):
        if self.tem_aresta(u, v):
            self.adj_list[u] = [(v2, p) for v2, p in self.adj_list[u] if v2 != v]
            self.tamanho -= 1

    def remove_vertice(self, u):
        if u in self.adj_list:
            # Diminui o tamanho com a quantidade de arestas que saem de u
            self.tamanho -= len(self.adj_list[u])
            
            # Remove o vértice
            del self.adj_list[u]
            self.ordem -= 1

            # Remove as arestas que chegam em u e atualiza o tamanho
            for vertice, vizinhos in self.adj_list.items():
                original_len = len(vizinhos)
                vizinhos[:] = [(v, p) for v, p in vizinhos if v != u]
                # Diminui o tamanho pela quantidade de arestas removidas
                self.tamanho -= (original_len - len(vizinhos)) 
 
   
    def tem_aresta(self, vertice1, vertice2):
        if vertice2 in dict(self.adj_list[vertice1]) and vertice1 in dict(self.adj_list[vertice2]):
            return True
        else:
            return False 

    def grau_entrada(self, u):
        return sum(
            1 for vizinhos in self.adj_list.values() if any(v == u for v, _ in vizinhos)
        )

    def grau_saida(self, u):
        return len(self.adj_list[u])

    def grau(self, u):
        return self.grau_entrada(u) + self.grau_saida(u)

    def get_peso(self, u, v):
        for vizinho, peso in self.adj_list[u]:
            if vizinho == v:
                return peso
        return None

    def imprime_lista_adjacencias(self):
        for u, vizinhos in self.adj_list.items():
            arestas = " -> ".join(f"({v}, {p})" for v, p in vizinhos)
            print(f"{u}: {arestas}")
