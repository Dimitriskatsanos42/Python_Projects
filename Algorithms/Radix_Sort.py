#Python program for implementation of Radix Sort
def countingSort(arr, exp):
    n = len(arr)

    # Εύρεση του μέγιστου αριθμού για τον καθορισμό του μεγέθους του counting array
    max_value = max(arr)
    
    # Δημιουργία του counting array
    count = [0] * (max_value + 1)
    
    # Μέτρηση της εμφάνισης των ψηφίων
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Υπολογισμός των αθροιστικών συχνοτήτων
    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    # Δημιουργία του τελικού ταξινομημένου πίνακα
    output = [0] * n
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    # Αντιγραφή του ταξινομημένου πίνακα στον αρχικό πίνακα
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr):
    # Εύρεση του μέγιστου αριθμού για τον καθορισμό του αριθμού των ψηφίων
    max_value = max(arr)

    # Εκτέλεση του Counting Sort για κάθε ψηφίο αριθμού (από το λιγότερο σημαντικό στο πιο σημαντικό)
    exp = 1
    while max_value // exp > 0:
        countingSort(arr, exp)
        exp *= 10

data = [170, 45, 75, 90, 802, 24, 2, 66]
print("Πριν την ταξινόμηση:")
print(data)
radixSort(data)
print("Μετά την ταξινόμηση:")
print(data)
