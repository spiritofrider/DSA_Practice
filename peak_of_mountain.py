def peakMountain(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    boundary_index = -1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] > nums[mid + 1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

print(peakMountain([2,4,6,5,3,1]))