# Bubble sort in Python

def bubble_sort(list):

    for i in range(len(list)):

        for j in range(0, len(list) - i - 1):

            if list[j] > list[j + 1]:

               temp = list[j]
               list[j] = list[j+1]
               list[j+1] = temp


list = [18, -2, 33,  45, 0, 11, 130]

bubble_sort(list)

print('Sorted Array in Ascending Order:')
print(list)
