def selection_sort(arr, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])


if __name__ == '__main__':
    arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
    size = len(arr)
    selection_sort(arr, size)
    print('The array after sorting in Ascending Order by selection sort is:')
    print(arr)
