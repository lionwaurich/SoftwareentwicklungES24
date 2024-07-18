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

def display_graph(G, pos, highlight_node=None, highlight_edges=None):
    plt.clf()  # Clear, damit das aktuelle fenster geschlossen wird
    node_colors = ['lightblue' if node != highlight_node else 'red' for node in G]
    edge_colors = ['red' if highlight_edges and (u, v) in highlight_edges else 'black' for u, v in G.edges]
    
    nx.draw(G, pos, with_labels=True, node_size=4000, node_color=node_colors, edge_color=edge_colors, font_size=12, font_weight='bold', arrowstyle='-|>', arrowsize=20)
    
    edge_labels = {((u, v)): f"{d['input']} / {d['output']}" for u, v, d in G.edges(data=True)}
    red_edge_labels = {((u, v)): f"{d['input']} / {d['output']}" for u, v, d in G.edges(data=True) if highlight_edges and (u, v) in highlight_edges}
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=red_edge_labels, font_color='red')
    
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
            highlight_edges = [(u, v) for u, v in G_de.edges if u == state]
            display_graph(G_de, pos_de, highlight_node=state, highlight_edges=highlight_edges)
        else:
            print("Zustand nicht gefunden. Bitte versuchen Sie es erneut.")

def main():
    # Öffnen der seriellen Verbindung (könnte abweichen bei verschiedenen geräten)
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
    
    # Zeige den Graphen ohne Markierungen zu beginn des PRogrammes
    plt.ion()
    fig, ax = plt.subplots(figsize=(16, 10))  # Erstelle eine Ausgabe (größe vllt anpassen bei anderen Bildschirmen 16x20 bsp)

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
        ser.close()  # serielle Port sauber schließen
        print("Serielle Verbindung geschlossen")

if __name__ == "__main__":
    main()
