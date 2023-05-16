def mergesort(array, left_index, right_index):
    if left_index >= right_index:
        return

    # Υπολογίζουμε τον δείκτη μέσου σημείου
    middle = (left_index + right_index) // 2

    # Αναδρομικά καλούμε τον αλγόριθμο mergesort για το αριστερό και το δεξί υποπίνακα
    mergesort(array, left_index, middle)
    mergesort(array, middle + 1, right_index)

    # Καλούμε τη συνάρτηση merge για να ενώσουμε τα δύο υποπίνακες
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):
    # Δημιουργούμε δύο υπολίστες από τον αρχικό πίνακα
    left_sublist = array[left_index:middle + 1]
    right_sublist = array[middle + 1:right_index + 1]

    # Αρχικοποιούμε δείκτες και τον δείκτη ταξινόμησης
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index

    # Συγκρίνουμε τα στοιχεία των δύο υπολιστών και τα τοποθετούμε στη σωστή θέση στον αρχικό πίνακα
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            array[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index += 1
        else:
            array[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index += 1

        sorted_index += 1

    # Αν υπάρχουν ακόμη στοιχεία στην αριστερή υπολίστα, τα τοποθετούμε στη σωστή θέση στον αρχικό πίνακα
    while left_sublist_index < len(left_sublist):
        array[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index += 1
        sorted_index += 1

    # Αν υπάρχουν ακόμη στοιχεία στη δεξιά υπολίστα, τα τοποθετούμε στη σωστή θέση στον αρχικό πίνακα
    while right_sublist_index < len(right_sublist):
        array[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index += 1
        sorted_index += 1

array = [56, 86, 1, 4, 64, 14, 73, 29, 12, 3, 17, 93, 34]

mergesort(array, 0, len(array) - 1)
print(array)
