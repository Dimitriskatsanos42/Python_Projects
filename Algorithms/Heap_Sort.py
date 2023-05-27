def heapify(arr, n, i):
    largest = i  # Υποθέτουμε ότι ο μεγαλύτερος κόμβος είναι ο i
    left = 2 * i + 1
    right = 2 * i + 2

    # Εάν ο αριστερός παιδίς είναι μεγαλύτερος από τον root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Εάν ο δεξιός παιδίς είναι μεγαλύτερος από τον root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Εάν ο largest δεν είναι πια ο root, τότε ανταλλάσουμε τα στοιχεία
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Αναδρομικά εφαρμόζουμε την heapify στον μεγαλύτερο κόμβο
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Κατασκευή του max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Εξαγωγή στοιχείου από το heap ένα-ένα και ταξινόμηση
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Ανταλλαγή του πρώτου και τελευταίου στοιχείου
        heapify(arr, i, 0)

data = [12, 45, 2, 9, 25, 15, 10,  32, 63, 78, 81]
heapSort(data)
print(data)
