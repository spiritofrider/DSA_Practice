def square_root_estimation(N:int) -> int:
    if N == 0:
        return 0
    left, right = 1,N
    boundary_index = -1

    while left <= right:
        mid = (left + right)//2

        if mid*mid == N:
            return mid
        elif mid*mid >= N:
            boundary_index = mid
            right = mid-1
        else:
            left = mid+1
    return boundary_index-1

print(square_root_estimation(2))