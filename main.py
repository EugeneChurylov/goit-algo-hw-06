import networkx as nx
import matplotlib.pyplot as plt

from metro_graph import create_metro_graph
from dfs import dfs
from bfs import bfs
from dijkstra import dijkstra


metro_graph = create_metro_graph()

#DFS
print("DFS")
start_node = "Академмістечко"
dfs(metro_graph, start_node)

pos = nx.get_node_attributes(metro_graph, 'pos')
plt.figure(figsize=(10, 8))
nx.draw(metro_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

plt.show()

#BFS
print(' ')
print("BFS")
start_node = "Академмістечко"
bfs(metro_graph, start_node)

pos = nx.get_node_attributes(metro_graph, 'pos')
plt.figure(figsize=(10, 8))
nx.draw(metro_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

plt.show()

# Dijkstra
shortest_paths = {}
for station in metro_graph.nodes:
    shortest_paths[station] = dijkstra(metro_graph, station)

# Виведення результатів
for source in shortest_paths:
    print(f"Найкоротші шляхи між станціями {source}:")
    for target, distance in shortest_paths[source].items():
        print(f"  {target}: {distance}")

# Відображення графа (з вагами)
pos = nx.get_node_attributes(metro_graph, 'pos')
plt.figure(figsize=(10, 8))
nx.draw(metro_graph, pos, with_labels=True, font_weight='bold',
        node_size=700, node_color='skyblue', font_size=8)
edge_labels = nx.get_edge_attributes(metro_graph, 'weight')
nx.draw_networkx_edge_labels(metro_graph, pos, edge_labels=edge_labels)
plt.show()