from collections import defaultdict

class Grafo():
  def __init__(self):
    self.adj_list = defaultdict(list)
    self.tamanho = 0  # Número de arestas
    self.ordem = 0    # Número de vértices

  def adiciona_vertice(self, vertice):
    if vertice in self.adj_list: # Verificação redudante apenas para existir um retorno da função, a adinção em defaultdict já verifica se existe ou não
      print("Vertice já existente!")
    else:
        self.adj_list[vertice] 
        self.ordem += 1  # Incrementa a ordem
        print(f"Vertice {vertice} inserido com sucesso!")

  def remove_vertice(self, vertice):
    if vertice  in dict(self.adj_list): # Verificação redudante apenas para existir um retorno da função, a adinção em defaultdict já verifica se existe ou não
        for v in self.adj_list:
          if self.tem_aresta(v, vertice):
            self.remove_aresta(v, vertice)
        self.adj_list.pop(vertice)
        self.ordem -= 1  # Decrementa a ordem
        print(f"Vertice {vertice} removido com sucesso!.")
    else:
        print(f"Vertice {vertice} não existe.")
        

  def adiciona_aresta(self, vertice1, vertice2, peso):
    # Verifica se os vértices existem, caso contrário, adiciona-os
    if vertice1 not in self.adj_list:
        self.adiciona_vertice(vertice1)
    if vertice2 not in self.adj_list:
        self.adiciona_vertice(vertice2)
    if not self.tem_aresta(vertice1, vertice2):
        self.adj_list[vertice1].append((vertice2, peso))
        self.adj_list[vertice2].append((vertice1, peso))
        self.tamanho += 1  # Incrementa o tamanho
        print(f"Aresta entre {vertice1} e {vertice2} Inserida com sucesso!")
    else:
        print(f"Aresta entre {vertice1} e {vertice2} já existe.")

  def remove_aresta(self, vertice1, vertice2):
    if self.tem_aresta(vertice1, vertice2):
        #Usa list comprehension pra filtrar o elemento a ser removido
        self.adj_list[vertice1] = [(v, w) for v, w in self.adj_list[vertice1] if v != vertice2]
        self.adj_list[vertice2] = [(v, w) for v, w in self.adj_list[vertice2] if v != vertice1]
        self.tamanho -= 1  # Decrementa o tamanho
        print(f"Aresta entre {vertice1} e {vertice2} removida.")
    else:
        print(f"Aresta entre {vertice1} e {vertice2} não existe.")


  def tem_aresta(self, vertice1, vertice2):
    if vertice2 in dict(self.adj_list[vertice1]) and vertice1 in dict(self.adj_list[vertice2]): 
        return True
    else:
        return False

  def grau_entrada(self, vertice):
    grau_entrada = 0
    for v in self.adj_list:
        if any(neighbor == vertice for neighbor, _ in self.adj_list[v]): # percorre a lista de adjacencia do vertice especifico
            grau_entrada +=1
    return grau_entrada

  def grau_saida(self, vertice):
    return len(self.adj_list[vertice])

  def grau(self, vertice):
    return self.grau_entrada(vertice) + self.grau_saida(vertice) 

  def imprime_lista_adjacencias(self):
    print(self.adj_list)
