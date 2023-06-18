import heapq

def dijkstra(graph, start):
    # Αρχικοποίηση των αποστάσεων με άπειρο
    distances = {node: float('inf') for node in graph}
    # Αρχικοποίηση της απόστασης του αρχικού κόμβου με 0
    distances[start] = 0
    # Ουρά προτεραιότητας για την επιλογή του επόμενου κόμβου
    pq = [(0, start)]

    while pq:
        # Εξαγωγή του κόμβου με την ελάχιστη απόσταση
        curr_dist, curr_node = heapq.heappop(pq)

        # Έλεγχος για τυχόν καλύτερη απόσταση για τους γείτονες
        for neighbor, edge_weight in graph[curr_node].items():
            distance = curr_dist + edge_weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Αποτελέσματα Dijkstra:")
for node, distance in distances.items():
    print(f"Απόσταση από τον κόμβο {start_node} στον κόμβο {node}: {distance}")
