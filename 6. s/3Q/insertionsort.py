def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)

arr = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
print(arr)
insertionSort(arr)
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])