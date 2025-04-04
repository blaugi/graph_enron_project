from collections import defaultdict

class Grafo():
    """
    Classe que representa um grafo com suporte a arestas direcionadas e nomeadas.
    """

    def __init__(self):
        """
        Inicializa o grafo com uma lista de adjacência, tamanho (número de arestas) e ordem (número de vértices).
        """
        self.adj_list = defaultdict(list)
        self.tamanho = 0  # Número de arestas
        self.ordem = 0    # Número de vértices

    def adiciona_vertice(self, vertice):
        """
        Adiciona um vértice ao grafo.

        Args:
            vertice: O identificador do vértice a ser adicionado.
        """
        if vertice in self.adj_list:  # Verificação redundante apenas para existir um retorno da função, a adição em defaultdict já verifica se existe ou não
            print("Vertice já existente!")
        else:
            self.adj_list[vertice]
            self.ordem += 1  # Incrementa a ordem
            print(f"Vertice {vertice} inserido com sucesso!")

    def remove_vertice(self, vertice):
        """
        Remove um vértice do grafo, incluindo todas as arestas conectadas a ele.

        Args:
            vertice: O identificador do vértice a ser removido.
        """
        if vertice in dict(self.adj_list):  # Verificação redundante apenas para existir um retorno da função, a adição em defaultdict já verifica se existe ou não
            for v in self.adj_list:
                if self.tem_aresta(v, vertice):
                    self.remove_aresta(v, vertice)
            self.adj_list.pop(vertice)
            self.ordem -= 1  # Decrementa a ordem
            print(f"Vertice {vertice} removido com sucesso!.")
        else:
            print(f"Vertice {vertice} não existe.")

    def adiciona_aresta(self, vertice1, vertice2, peso, nome=None, direcionada=False):
        """
        Adiciona uma aresta ao grafo.

        Args:
            vertice1: O vértice de origem.
            vertice2: O vértice de destino.
            peso: O peso da aresta.
            nome: (Opcional) O nome da aresta.
            direcionada: (Opcional) Indica se a aresta é direcionada.
        """
        if not self.tem_aresta(vertice1, vertice2):
            self.adj_list[vertice1].append((vertice2, peso, nome))
            if not direcionada:
                self.adj_list[vertice2].append((vertice1, peso, nome))
            self.tamanho += 1  # Incrementa o tamanho
            print(f"Aresta {'direcionada' if direcionada else 'não direcionada'} entre {vertice1} e {vertice2} inserida com sucesso!")
        else:
            print(f"Aresta entre {vertice1} e {vertice2} já existe.")

    def remove_aresta(self, vertice1, vertice2, direcionada=False):
        """
        Remove uma aresta do grafo.

        Args:
            vertice1: O vértice de origem.
            vertice2: O vértice de destino.
            direcionada: (Opcional) Indica se a aresta é direcionada.
        """
        if self.tem_aresta(vertice1, vertice2):
            self.adj_list[vertice1] = [(v, w, n) for v, w, n in self.adj_list[vertice1] if v != vertice2]
            if not direcionada:
                self.adj_list[vertice2] = [(v, w, n) for v, w, n in self.adj_list[vertice2] if v != vertice1]
            self.tamanho -= 1  # Decrementa o tamanho
            print(f"Aresta {'direcionada' if direcionada else 'não direcionada'} entre {vertice1} e {vertice2} removida.")
        else:
            print(f"Aresta entre {vertice1} e {vertice2} não existe.")

    def tem_aresta(self, vertice1, vertice2):
        """
        Verifica se existe uma aresta entre dois vértices.

        Args:
            vertice1: O vértice de origem.
            vertice2: O vértice de destino.

        Returns:
            bool: True se a aresta existir, False caso contrário.
        """
        return any(v == vertice2 for v, _, _ in self.adj_list[vertice1])

    def grau_entrada(self, vertice):
        """
        Calcula o grau de entrada de um vértice.

        Args:
            vertice: O vértice para o qual calcular o grau de entrada.

        Returns:
            int: O grau de entrada do vértice.
        """
        grau_entrada = 0
        for v in self.adj_list:
            if any(neighbor == vertice for neighbor, _, _ in self.adj_list[v]):  # percorre a lista de adjacência do vértice específico
                grau_entrada += 1
        return grau_entrada

    def grau_saida(self, vertice):
        """
        Calcula o grau de saída de um vértice.

        Args:
            vertice: O vértice para o qual calcular o grau de saída.

        Returns:
            int: O grau de saída do vértice.
        """
        return len(self.adj_list[vertice])

    def grau(self, vertice):
        """
        Calcula o grau total de um vértice.

        Args:
            vertice: O vértice para o qual calcular o grau total.

        Returns:
            int: O grau total do vértice.
        """
        return self.grau_entrada(vertice) + self.grau_saida(vertice)

    def imprime_lista_adjacencias(self):
        """
        Imprime a lista de adjacências do grafo.
        """
        print(self.adj_list)
