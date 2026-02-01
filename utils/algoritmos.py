import heapq

def dijkstra(grafo, origen, destino):
    heap = [(0, origen, [])]  # (costo acumulado, nodo actual, ruta)
    visitados = set()

    while heap:
        costo, nodo, ruta = heapq.heappop(heap)
        if nodo in visitados:
            continue
        ruta = ruta + [nodo]
        if nodo == destino:
            return costo, ruta
        visitados.add(nodo)
        for vecino, peso in grafo.get(nodo, {}).items():
            if vecino not in visitados:
                heapq.heappush(heap, (costo + peso, vecino, ruta))
    return float('inf'), []

def bfs(grafo, inicio):
    visitados = set()
    cola = [inicio]
    orden = []

    while cola:
        nodo = cola.pop(0)
        if nodo not in visitados:
            visitados.add(nodo)
            orden.append(nodo)
            cola.extend([v for v in grafo.get(nodo, {}) if v not in visitados])
    return orden

def dfs(grafo, inicio, visitados=None, orden=None):
    if visitados is None:
        visitados = set()
    if orden is None:
        orden = []
    visitados.add(inicio)
    orden.append(inicio)
    for vecino in grafo.get(inicio, {}):
        if vecino not in visitados:
            dfs(grafo, vecino, visitados, orden)
    return orden
