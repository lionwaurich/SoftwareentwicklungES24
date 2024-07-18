import matplotlib.pyplot as plt
import networkx as nx
import serial
import time

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
    plt.draw()  # Update the plot instead of show (bessere Graphen ansicht)

def main():
    ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
    plt.ion()
    
    filename = "config.txt"  # Pfad zur Konfigurationsdatei
    nodes, edges = read_graph_configuration(filename)
    G_de, pos_de = create_graph(nodes, edges)
    display_graph(G_de, pos_de)  # Zeige den initialen Graphen ohne Markierungen
    
    try:
        while True:
            if ser.in_waiting > 0:
                state = ser.readline().decode('utf-8').strip()
                if state.lower() == 'q':
                    print("Programm wird beendet.")
                    break
                elif state in G_de:
                    plt.close()
                    display_graph(G_de, pos_de, highlight_node=state)
                else:
                    print("Zustand nicht gefunden. Bitte versuchen Sie es erneut.")
            time.sleep(0.1)  # Kurze Pause, um das Graphenfenster zu aktualisieren
    finally:
        ser.close()  # Stelle sicher, dass der serielle Port sauber geschlossen wird

if __name__ == "__main__":
    main()
