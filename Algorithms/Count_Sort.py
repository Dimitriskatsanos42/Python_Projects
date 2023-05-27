def countingSort(arr):
    # Βρίσκουμε το μέγιστο στοιχείο της λίστας
    max_val = max(arr)

    # Δημιουργούμε έναν πίνακα καταμέτρησης μεγέθους max_val+1,
    # αρχικοποιημένο με μηδενικά
    count = [0] * (max_val + 1)

    # Υπολογίζουμε την συχνότητα εμφάνισης κάθε στοιχείου
    for num in arr:
        count[num] += 1

    # Ανακατανέμουμε τα στοιχεία στην τελική λίστα
    i = 0
    for num in range(max_val + 1):
        while count[num] > 0:
            arr[i] = num
            i += 1
            count[num] -= 1

data = [-5, -10, 0, -3, 8, 5, -1, 10,  32, 63, 78, 81]
countingSort(data)
print(data)
