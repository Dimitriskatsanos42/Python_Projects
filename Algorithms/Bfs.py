from collections import deque

def bfs(graph, start):
    visited = set()  # Κρατάμε τα κόμβους που έχουμε επισκεφτεί
    queue = deque([start])  # Ουρά για την αποθήκευση των κόμβων προς εξερεύνηση

    while queue:
        node = queue.popleft()  # Αφαιρούμε τον πρώτο κόμβο από την ουρά
        print(node)  # Εκτυπώνουμε τον κόμβο (ή κάνουμε άλλη επεξεργασία)

        if node not in visited:
            visited.add(node)  # Επισημειώνουμε τον κόμβο ως επισκεπτόμενο
            neighbors = graph[node]  # Βρίσκουμε τους γείτονες του κόμβου

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)  # Προσθέτουμε τους γείτονες στην ουρά

# Παράδειγμα χρήσης
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS traversal:")
bfs(graph, 'A')
