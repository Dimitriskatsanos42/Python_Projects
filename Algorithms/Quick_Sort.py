# Quick sort in Python

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Επιλογή του pivot ως το μεσαίο στοιχείο
    lesser, equal, greater = [], [], []

    for num in arr:
        if num < pivot:
            lesser.append(num)  # Προσθήκη του στοιχείου στη λίστα των μικρότερων από το pivot
        elif num == pivot:
            equal.append(num)  # Προσθήκη του στοιχείου στη λίστα των ίσων με το pivot
        else:
            greater.append(num)  # Προσθήκη του στοιχείου στη λίστα των μεγαλύτερων από το pivot

    # Αναδρομική κλήση της quickSort για τις λίστες των μικρότερων και μεγαλύτερων αριθμών,
    # συνδυασμένες με την λίστα των ίσων, για την τελική ταξινόμηση
    return quickSort(lesser) + equal + quickSort(greater)

data = [17, 45, 2, 9, 23, 15, 52, 67, 50, 73]
sorted_data = quickSort(data)
print(sorted_data)
