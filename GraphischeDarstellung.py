import matplotlib.pyplot as plt
import networkx as nx


G_de = nx.DiGraph()

# Zustände und Übergänge definieren (übersetzt)
edges_de = [
    ("WARTET", "VALIDIERUNG", {"input": "KARTE_EINFÜHREN", "output": ""}),
    ("VALIDIERUNG", "BEZAHLT", {"input": "ZAHLUNG_BESTÄTIGT", "output": "TOR_ÖFFNEN"}),
    ("VALIDIERUNG", "NICHT_BEZAHLT", {"input": "ZAHLUNG_VERWEIGERT", "output": "ZAHLUNG_AUFFORDERN"}),
    ("BEZAHLT", "WARTET", {"input": "", "output": ""}),
    ("NICHT_BEZAHLT", "WARTET", {"input": "", "output": ""})
]

# Kanten zum Graph hinzufügen
G_de.add_edges_from(edges_de)

# Position der Knoten für eine übersichtliche Darstellung
pos_de = {
    "WARTET": (0, 0),
    "VALIDIERUNG": (1, 0),
    "BEZAHLT": (2, 1),
    "NICHT_BEZAHLT": (2, -1)
}

# Zeichnen des Graphen
plt.figure(figsize=(10, 5))
nx.draw(G_de, pos_de, with_labels=True, node_size=3000, node_color="skyblue", font_size=9, font_weight='bold', arrowstyle='-|>', arrowsize=20)
labels_de = nx.get_edge_attributes(G_de, "input")
nx.draw_networkx_edge_labels(G_de, pos_de, edge_labels=labels_de, font_color='green')

# Zeige Ausgaben auf den Kanten
edge_labels_de = {((u, v)): f"{d['input']} / {d['output']}" for u, v, d in G_de.edges(data=True)}
nx.draw_networkx_edge_labels(G_de, pos_de, edge_labels=edge_labels_de, label_pos=0.5, font_color='red')

# Zeige den Graph
plt.title("Zustandsübergangsdiagramm")
plt.axis('off') # Achsen ausblenden für eine sauberere Darstellung
plt.show()
