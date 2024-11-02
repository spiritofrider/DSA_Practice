def firstTrueSortedBoolArray(arr):
    left, right = 0, len(arr) - 1
    boundary_value = -1

    while left <= right:
        mid = (left + right)//2
        if arr[mid]:
            boundary_value = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_value


print(firstTrueSortedBoolArray([False, False, False, True, True, True]))