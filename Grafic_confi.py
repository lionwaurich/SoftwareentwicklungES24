import matplotlib.pyplot as plt
import networkx as nx

def read_graph_configuration(filename):
    with open(filename, 'r') as file:
        content = file.read().split('#')
        nodes_info = content[0].strip().split('\n')
        edges_info = content[1].strip().split('\n')
    
    nodes = [tuple(node.split(',')) for node in nodes_info]
    edges = [tuple(edge.split(',')) for edge in edges_info]
    
    return nodes, edges

def create_graph(nodes, edges):
    G = nx.DiGraph()
    pos = {}
    for node, x, y in nodes:
        G.add_node(node)
        pos[node] = (float(x), float(y))
    
    for edge in edges:
        if len(edge) == 4:
            G.add_edge(edge[0], edge[1], input=edge[2], output=edge[3])
        else:
            G.add_edge(edge[0], edge[1], input='', output='')
    
    return G, pos

# Hauptlogik zum Einlesen der Konfiguration und Darstellen des Graphen
nodes, edges = read_graph_configuration('graph_config.txt')
G_de, pos_de = create_graph(nodes, edges)

# Zeichnen des Graphen
plt.figure(figsize=(10, 5))
nx.draw(G_de, pos_de, with_labels=True, node_size=3000, node_color="skyblue", font_size=9, font_weight='bold', arrowstyle='-|>', arrowsize=20)
edge_labels_de = {((u, v)): f"{d['input']} / {d['output']}" for u, v, d in G_de.edges(data=True)}
nx.draw_networkx_edge_labels(G_de, pos_de, edge_labels=edge_labels_de, label_pos=0.5, font_color='red')

plt.title("Zustandsübergangsdiagramm")
plt.axis('off')
plt.show()
