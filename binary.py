def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return 'NO VALUE'


n = [1, 3, 5, 6, 7, 11, 12, 22, 33, 45, 67, 69]
print(binary_search(n, 67))
