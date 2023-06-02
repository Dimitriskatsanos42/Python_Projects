# using bucket sort 
def insertionSort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucketSort(arr):
    # Δημιουργία κενών κάδων
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    # Τοποθέτηση των στοιχείων στους κάδους
    for num in arr:
        index = int(num * num_buckets)
        buckets[index].append(num)

    # Ταξινόμηση των στοιχείων κάθε κάδου με τη χρήση Insertion Sort
    for bucket in buckets:
        insertionSort(bucket)

    # Επανατοποθέτηση των στοιχείων στον αρχικό πίνακα
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

    return arr

# Παράδειγμα χρήσης
array = [0.42, 0.32, 0.75, 0.12, 0.98, 0.63]
sorted_array = bucketSort(array)
print(sorted_array)
