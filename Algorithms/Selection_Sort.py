def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        # Βρίσκουμε το ελάχιστο στοιχείο στον υπόλοιπο υποπίνακα
        for i in range(step + 1, size):
            # Για να ταξινομήσουμε φθίνουσα, αλλάξτε το > σε < σε αυτήν τη γραμμή
            # Επιλέγουμε το ελάχιστο στοιχείο σε κάθε επανάληψη
            if array[i] < array[min_idx]:
                min_idx = i

        # Ανταλλάσσουμε το ελάχιστο στοιχείο με το πρώτο στοιχείο του υποπίνακα
        (array[step], array[min_idx]) = (array[min_idx], array[step])

array = [-10, 65, 3, 34, -70, 49, -5, 91]
size = len(array)
selectionSort(array, size)
print(array)