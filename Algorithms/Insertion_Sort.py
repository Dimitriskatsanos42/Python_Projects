def insertionSort(array):
    # Ξεκινάμε από το δεύτερο στοιχείο του πίνακα
    for i in range(1, len(array)):
        key = array[i]  # Το τρέχον στοιχείο που θα εισαχθεί στο σωστό του θέση

        j = i - 1
        # Μετακινούμε όλα τα στοιχεία μεγαλύτερα από το key μια θέση δεξιότερα
        # μέχρι να βρεθεί η σωστή θέση για το key
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key 

array = [32, 9, 20, 57, 69, 91, 4]
insertionSort(array)
print(array)
