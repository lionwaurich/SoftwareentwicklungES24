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

def display_graph(G, pos, highlight_node=None):
    plt.figure(figsize=(10, 5))
    node_colors = ['lightblue' if node != highlight_node else 'red' for node in G]
    edge_colors = ['black' if (u != highlight_node) else 'red' for u, v in G.edges]
    
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color=node_colors, edge_color=edge_colors, font_size=9, font_weight='bold', arrowstyle='-|>', arrowsize=20)
    edge_labels = {((u, v)): f"{d['input']} / {d['output']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red' if highlight_node else 'black')
    plt.title("Zustandsübergangsdiagramm")
    plt.axis('off')
    plt.draw()  # Update the plot instead of show

# Start des interaktiven Modus
plt.ion()

# Hauptlogik zum Einlesen der Konfiguration und Darstellen des Graphen
filename = input("Bitte geben Sie den Dateinamen ein: ")
nodes, edges = read_graph_configuration(filename)
G_de, pos_de = create_graph(nodes, edges)

# Zeige den initialen Graphen ohne Markierungen
display_graph(G_de, pos_de)

while True:
    plt.pause(0.1)  # Kurze Pause, um das Graphenfenster zu aktualisieren
    state = input("Bitte geben Sie den Zustandsnamen ein (drücken Sie 'q' zum Beenden): ").strip()
    if state.lower() == 'q':
        print("Programm wird beendet.")
        break
    elif state in G_de:
        plt.close()  # Schließt das aktuelle Fenster
        display_graph(G_de, pos_de, highlight_node=state)
    else:
        print("Zustand nicht gefunden. Bitte versuchen Sie es erneut.")
