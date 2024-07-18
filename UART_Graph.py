import matplotlib.pyplot as plt
import networkx as nx
import serial
import threading
import queue
from matplotlib.animation import FuncAnimation
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
    plt.clf()  # Clear the current figure
    node_colors = ['lightblue' if node != highlight_node else 'red' for node in G]
    edge_colors = ['red' if highlight_node and highlight_node in [u, v] else 'black' for u, v in G.edges]
    
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color=node_colors, edge_color=edge_colors, font_size=9, font_weight='bold', arrowstyle='-|>', arrowsize=20)
    edge_labels = {((u, v)): f"{d['input']} / {d['output']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red' if highlight_node else 'black')
    plt.title("Zustandsübergangsdiagramm")
    plt.axis('off')
    plt.draw()

def serial_listener(ser, q):
    while True:
        if ser.in_waiting > 0:
            try:
                state = ser.readline().decode('utf-8').strip()
                q.put(state)
            except Exception as e:
                print(f"Fehler beim Lesen der seriellen Daten: {e}")
        time.sleep(0.1)

def update_graph(frame, G_de, pos_de, q):
    if not q.empty():
        state = q.get()
        print("Empfangen:", state)  # Debugging-Ausgabe
        if state.lower() == 'q':
            print("Programm wird beendet.")
            plt.close()
        elif state in G_de:
            display_graph(G_de, pos_de, highlight_node=state)
        else:
            print("Zustand nicht gefunden. Bitte versuchen Sie es erneut.")

def main():
    # Öffnen der seriellen Verbindung
    try:
        ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
        print("Serielle Verbindung geöffnet")
    except serial.SerialException as e:
        print(f"Fehler beim Öffnen der seriellen Verbindung: {e}")
        return
    
    # Einlesen der Konfigurationsdatei und Erstellen des Graphen
    filename = "config.txt"
    nodes, edges = read_graph_configuration(filename)
    G_de, pos_de = create_graph(nodes, edges)
    
    # Zeige den initialen Graphen ohne Markierungen
    plt.ion()
    fig, ax = plt.subplots()  # Erstelle ein neues Fenster

    display_graph(G_de, pos_de)

    # Queue für die serielle Kommunikation
    q = queue.Queue()
    listener_thread = threading.Thread(target=serial_listener, args=(ser, q))
    listener_thread.daemon = True
    listener_thread.start()
    
    ani = FuncAnimation(fig, update_graph, fargs=(G_de, pos_de, q), interval=100, cache_frame_data=False)
    
    try:
        plt.show(block=True)
    finally:
        ser.close()  # Stelle sicher, dass der serielle Port sauber geschlossen wird
        print("Serielle Verbindung geschlossen")

if __name__ == "__main__":
    main()
