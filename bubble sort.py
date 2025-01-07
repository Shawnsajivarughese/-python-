def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

arr = [78, 57, 35, 17, 22, 11, 98]
print("Sorted array is:", bubble_sort(arr))
