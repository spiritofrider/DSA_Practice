def find_first_occurence(arr, target):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while(left <= right):
        mid = (left + right)//2
        if arr[mid] == target:
            boundary_index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return boundary_index

print(find_first_occurence([1,3,3,5,7,9], 7))