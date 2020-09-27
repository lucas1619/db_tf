from lista import DoubleLinkedList
#crear el grafo
class Quoridor:
  def init(self, n=5, q_players = 2):

        self.n = n
        self.q_nodos = n*n
        self.q_players = 2
        self.grafo = [DoubleLinkedList() for i in range(self.q_nodos)]
        for i, nodo in enumerate(self.grafo):
          if i % n != n - 1:
            self.grafo[i].push_back(i + 1)
            self.grafo[i + 1].push_back(i)
          if i + n < n*n:
            self.grafo[i].push_back(i+n)
            self.grafo[i + n].push_back(i)

  def dicionario(self):
      dic = []
      listaN = [x for x in range(self.q_nodos)]
      for i, nodo in enumerate(self.grafo):
          data = (list(nodo))
          dic.append(data)
      diccio = (dict(zip(listaN, dic)))
      return diccio

  def dijsktra(self, Nodos):

    grafo = self.dicionario()

    S = [];
    Queue = [];
    anterior = [0 for i in range(max(grafo) +1)];
    distancia = [0 for i in range(max(grafo) +1)]

    for nodo in grafo:
        distancia[nodo] = 10000
        Queue.append(nodo)
    distancia[Nodos[0]] = 0

    while not len(Queue) == 0:
        distancia_minima = 10000
        for nodo in Queue:
            if distancia[nodo] < distancia_minima:
                distancia_minima = distancia[nodo]
                nodo_temporal = nodo
        nodo_distancia_minima = nodo_temporal
        Queue.remove(nodo_distancia_minima)

        for vecino in grafo[nodo_distancia_minima]:
            if distancia[nodo_distancia_minima] == 10000:
                distancia_temporal = 0
            else:
                distancia_temporal = distancia[nodo_distancia_minima]
            distancia_con_peso = distancia_temporal + 1
            if distancia_con_peso < distancia[vecino]:
                distancia[vecino] = distancia_con_peso
                anterior[vecino] = nodo_distancia_minima

        if nodo_distancia_minima == Nodos[1]:
            if anterior[nodo_distancia_minima] != 0 or nodo_distancia_minima == Nodos[0]:
                while nodo_distancia_minima != 0:
                    S.insert(0, nodo_distancia_minima)
                    nodo_distancia_minima = anterior[nodo_distancia_minima]
                return S

  def bellman_ford(self, start, end):
    ruta = DoubleLinkedList()
    ruta.push_front(end)
    
    distancia = [float("Inf") for x in range(self.q_nodos)]
    
    previo = [-1 for x in range(self.q_nodos)]
    print(previo)
    distancia[start] = 0
    for iteracion in range(self.q_nodos - 1):
      for actual, nodo in enumerate(self.grafo):
        for adyacente in nodo:
          if distancia[actual] + 1 < distancia[adyacente]:
            distancia[adyacente] = distancia[actual] + 1
            previo[adyacente] = actual
    anterior = previo[end]
    while anterior != -1:
      ruta.push_front(anterior)
      anterior = previo[anterior]
    return list(ruta)


jess = Quoridor()
jess.init(5)
print("5*5----------")
print(f"ruta de 0 a 24 --> {jess.dijsktra((0, 24))}")
print(f"ruta de 22 a 5 --> {jess.dijsktra((22, 5))}")
print(f"ruta de 23 a 9 --> {jess.dijsktra((23, 9))}")

print("4*4----------")
jess.init(4)

print(f"ruta de 0 a 12 --> {jess.dijsktra((0, 12))}")
print(f"ruta de 1 a 9 --> {jess.dijsktra((1, 9))}")
print(f"ruta de 3 a 15 --> {jess.dijsktra((3, 15))}")

print("9*9----------")
jess.init(9)

print(f"ruta de 6 a 76 --> {jess.dijsktra((6, 76))}")
print(f"ruta de 3 a 15 --> {jess.dijsktra((3, 15))}")
print(f"ruta de 6 a 64 --> {jess.dijsktra((6, 64))}")

jess.init(3)

print(f"ruta de 1 a 7 --> {jess.dijsktra((1, 7))}")


print("9*9----------")
print(jess.bellman_ford(1,4))