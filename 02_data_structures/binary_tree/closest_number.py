def find_closest_num(A, target):
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    min_diff = min_diff_left = min_diff_right = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None

    while low <= high:
        mid = (low + high) // 2
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid + 1] - target) 
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]

        else:
            return A[mid]
    return closest_num

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]
print(find_closest_num(A1, 11))
print(find_closest_num(A2, 4))