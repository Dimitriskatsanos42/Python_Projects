def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Επιστρέφει τη θέση του στοιχείου στον πίνακα
    return -1  # Επιστρέφει -1 αν το στοιχείο δεν βρεθεί

# Παράδειγμα χρήσης
array = [4, 2, 9, 7, 1, 5]
target = 7

result = linearSearch(array, target)

if result != -1:
    print(f"Το στοιχείο {target} βρίσκεται στη θέση {result} του πίνακα.")
else:
    print(f"Το στοιχείο {target} δεν βρέθηκε στον πίνακα.")
