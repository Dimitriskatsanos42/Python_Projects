# Shell sort in python
def shellSort(arr):
    n = len(arr)
    gap = n // 2

    # Έναρξη του βασικού βρόχου Shell Sort
    while gap > 0:
        # Εκτέλεση του Insertion Sort με το συγκεκριμένο διάστημα (gap)
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Ταξινόμηση των στοιχείων με χρήση της εισαγωγής (insertion sort)
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        # Μείωση του διαστήματος (gap) για το επόμενο βήμα ταξινόμησης
        gap //= 2

data = [9, 5, 1, 8, 3, 10, 4, 2, 7, 6]
print("Πριν την ταξινόμηση:")
print(data)
shellSort(data)
print("Μετά την ταξινόμηση:")
print(data)
