def findMinRoatatedSortedArr(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

print(findMinRoatatedSortedArr([30,40,50,10,20]))
print(findMinRoatatedSortedArr([3, 5, 7, 11, 13, 17, 19, 2]))