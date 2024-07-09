import matplotlib.pyplot as plt
import networkx as nx

def read_graph_configuration(filename):
    with open(filename, 'r') as file:
        content = file.read().split('#')
        nodes_info = content[0].strip().split('\n')
        edges_info = content[1].strip().split('\n')
    
    nodes = [tuple(node.split(',')) for node in nodes_info if node.strip()]
    edges = [tuple(edge.split(',')) for edge in edges_info if edge.strip()]
    
    return nodes, edges

def create_graph(nodes, edges):
    G = nx.DiGraph()
    pos = {}
    for node, x, y in nodes:
        G.add_node(node)
        pos[node] = (float(x), float(y))
    
    for edge in edges:
        G.add_edge(edge[0], edge[1], input=edge[2] if len(edge) > 2 else '', output=edge[3] if len(edge) > 3 else '')
    
    return G, pos

def draw_initial_graph(G, pos):
    plt.figure(figsize=(10, 5))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=9, font_weight='bold', arrowstyle='-|>', arrowsize=20)
    edge_labels = {((u, v)): f"{d['input']} / {d['output']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Zustandsübergangsdiagramm")
    plt.axis('off')
    plt.show()

def highlight_state_and_edges(G, pos, state):
    plt.figure(figsize=(10, 5))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=9, font_weight='bold', arrowstyle='-|>', arrowsize=20)
    outgoing_edges = list(G.out_edges(state))
    nx.draw_networkx_nodes(G, pos, nodelist=[state], node_size=3000, node_color="red")
    nx.draw_networkx_edges(G, pos, edgelist=outgoing_edges, edge_color="red", width=2)
    edge_labels = {((u, v)): f"{d['input']} / {d['output']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Zustandsübergangsdiagramm")
    plt.axis('off')
    plt.show()

# Hauptlogik zum Einlesen der Konfiguration und Darstellen des Graphen
filename = input("Bitte geben Sie den Dateinamen ein: ")
nodes, edges = read_graph_configuration(filename)
G_de, pos_de = create_graph(nodes, edges)

# Zeige den initialen Graphen ohne Markierungen
draw_initial_graph(G_de, pos_de)

while True:
    state = input("Bitte geben Sie den Zustandsnamen ein (drücken Sie 'q' zum Beenden): ")
    if state.lower() == 'q':
        break
    if state in G_de:
        highlight_state_and_edges(G_de, pos_de, state)
    else:
        print("Zustand nicht gefunden. Bitte versuchen Sie es erneut.")
