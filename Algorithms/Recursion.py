def recursion_example(n):
    if n <= 0:
        return
    print("Αριθμός:", n)
    recursion_example(n - 1)

# Κλήση της συνάρτησης recursion_example με παράδειγμα αριθμού
recursion_example(5)
