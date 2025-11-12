import networkx as nx
import matplotlib.pyplot as plt

"""
EJERCICIO – PUNTO 4: DIJKSTRA (Rutas de Transporte)
Autores: Adrian Carrillo y Kevin Candela

PREGUNTAS:
a) Representar el sistema como un grafo ponderado.
b) Usar el algoritmo de Dijkstra para encontrar la ruta más corta de Bogotá a Bucaramanga.
c) Explicar cómo cambia el resultado si se añade una nueva carretera Medellín–Bucaramanga (2 min).

RESPUESTAS:

a) Grafo ponderado:
   Ciudades conectadas por carreteras con tiempos en minutos.
   Bogotá–Medellín (6), Bogotá–Cali (4),
   Medellín–Barranquilla (5), Cali–Barranquilla (10),
   Cali–Bucaramanga (7), Barranquilla–Bucaramanga (3).

b) SIN la nueva carretera:
   Ruta más corta → Bogotá → Cali → Bucaramanga
   Tiempo total → 11 minutos

c) CON la nueva carretera Medellín–Bucaramanga (2 min):
   Ruta más corta → Bogotá → Medellín → Bucaramanga
   Tiempo total → 8 minutos

Este código genera el grafo y resalta el camino óptimo según Dijkstra.
"""

# Crear el grafo NO dirigido (las carreteras son bidireccionales)
G = nx.Graph()

# Aristas con pesos (tiempo en minutos)
edges = [
    ("Bogotá", "Medellín", 6),
    ("Bogotá", "Cali", 4),
    ("Medellín", "Barranquilla", 5),
    ("Cali", "Barranquilla", 10),
    ("Cali", "Bucaramanga", 7),
    ("Barranquilla", "Bucaramanga", 3),
    # Nueva carretera añadida:
    ("Medellín", "Bucaramanga", 2)
]

# Agregar aristas al grafo
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Calcular el camino más corto con Dijkstra (minimiza tiempo)
shortest_path = nx.dijkstra_path(G, "Bogotá", "Bucaramanga", weight="weight")
path_edges = list(zip(shortest_path, shortest_path[1:]))

print("Camino óptimo (menor tiempo):", shortest_path)

# Posiciones manuales para que se vea claro
pos = {
    "Bogotá": (0, 0),
    "Medellín": (2, 1),
    "Cali": (2, -1),
    "Barranquilla": (4, 0),
    "Bucaramanga": (6, 0)
}

plt.figure(figsize=(9, 5))
plt.title("Grafo de Ciudades y Rutas de Transporte (Dijkstra)", fontsize=13)

# Dibujar nodos
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="#1f78b4")
nx.draw_networkx_labels(G, pos, font_color="white", font_size=10)

# Dibujar TODAS las aristas (gris)
nx.draw_networkx_edges(G, pos, edge_color="gray", width=2)

# Resaltar el camino óptimo en negro
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="black", width=3)

# Etiquetas de pesos (tiempos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="black")

plt.axis("off")
plt.tight_layout()
plt.show()
